import sqlite3
from textwrap import dedent

QUERIES = [
    (
        "Top customers by lifetime spend",
        dedent(
            """
            SELECT c.customer_id, c.name, c.email, SUM(o.total_amount) AS lifetime_spend
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            GROUP BY c.customer_id
            ORDER BY lifetime_spend DESC
            LIMIT 5;
            """
        ),
    ),
    (
        "Best selling products by quantity",
        dedent(
            """
            SELECT p.product_id, p.name, p.category, SUM(oi.qty) AS total_sold
            FROM products p
            JOIN order_items oi ON p.product_id = oi.product_id
            GROUP BY p.product_id
            ORDER BY total_sold DESC
            LIMIT 10;
            """
        ),
    ),
    (
        "Monthly revenue",
        dedent(
            """
            SELECT substr(order_date,1,7) AS month, SUM(total_amount) AS revenue
            FROM orders
            GROUP BY month
            ORDER BY month;
            """
        ),
    ),
    (
        "Monthly composite analytics",
        dedent(
            """\
            WITH monthly_orders AS (
                SELECT substr(order_date, 1, 7) AS month,
                       SUM(total_amount) AS total_revenue,
                       COUNT(*) AS orders_count
                FROM orders
                GROUP BY month
            ),
            product_monthly AS (
                SELECT substr(o.order_date, 1, 7) AS month,
                       oi.product_id,
                       SUM(oi.qty) AS qty_sold
                FROM order_items AS oi
                JOIN orders AS o ON o.order_id = oi.order_id
                GROUP BY month, oi.product_id
            ),
            top_products AS (
                SELECT month,
                       product_id,
                       qty_sold
                FROM (
                    SELECT pm.*,
                           ROW_NUMBER() OVER (
                               PARTITION BY pm.month
                               ORDER BY pm.qty_sold DESC, pm.product_id
                           ) AS rn
                    FROM product_monthly AS pm
                )
                WHERE rn = 1
            ),
            monthly_reviews AS (
                SELECT substr(o.order_date, 1, 7) AS month,
                       r.product_id,
                       AVG(r.rating) AS avg_rating
                FROM reviews AS r
                JOIN order_items AS oi ON oi.product_id = r.product_id
                JOIN orders AS o
                    ON o.order_id = oi.order_id
                   AND o.customer_id = r.customer_id
                GROUP BY month, r.product_id
            )
            SELECT mo.month,
                   mo.total_revenue,
                   mo.orders_count,
                   tp.product_id AS top_product_id,
                   p.name AS top_product_name,
                   mr.avg_rating AS avg_rating_for_top_product
            FROM monthly_orders AS mo
            LEFT JOIN top_products AS tp ON tp.month = mo.month
            LEFT JOIN products AS p ON p.product_id = tp.product_id
            LEFT JOIN monthly_reviews AS mr
                ON mr.month = mo.month
               AND mr.product_id = tp.product_id
            ORDER BY mo.month
            LIMIT 12;
            """
        ),
    ),
]


def format_table(headers, rows):
    widths = [len(header) for header in headers]
    for row in rows:
        for idx, value in enumerate(row):
            widths[idx] = max(widths[idx], len(str(value)))

    def format_row(row_values):
        return " | ".join(str(value).ljust(widths[idx]) for idx, value in enumerate(row_values))

    lines = [format_row(headers), "-+-".join("-" * w for w in widths)]
    for row in rows:
        lines.append(format_row(row))
    return "\n".join(lines)


def main():
    conn = sqlite3.connect("ecom.db")
    try:
        for title, sql in QUERIES:
            cur = conn.execute(sql)
            rows = cur.fetchall()
            headers = [col[0] for col in cur.description]
            print(f"\n=== {title} ===")
            if rows:
                print(format_table(headers, rows))
            else:
                print("No rows returned")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
