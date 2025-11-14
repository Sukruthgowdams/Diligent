-- Top customers by total spend
SELECT c.customer_id,
       c.first_name || " " || c.last_name AS customer_name,
       SUM(o.total_amount) AS total_spend
FROM customers AS c
JOIN orders AS o ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spend DESC
LIMIT 10;

-- Best selling products by quantity
SELECT p.product_id,
       p.name,
       SUM(oi.quantity) AS units_sold
FROM products AS p
JOIN order_items AS oi ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY units_sold DESC
LIMIT 10;

-- Monthly revenue trend
SELECT substr(o.order_date, 1, 7) AS month,
       SUM(o.total_amount) AS revenue
FROM orders AS o
GROUP BY month
ORDER BY month;
