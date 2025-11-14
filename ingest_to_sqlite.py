import csv
import sqlite3
from pathlib import Path

DB_NAME = "ecom.db"
CSV_CONFIG = {
    "customers": {
        "file": "customers.csv",
        "columns": ["customer_id", "name", "email", "join_date", "city"],
    },
    "products": {
        "file": "products.csv",
        "columns": ["product_id", "name", "category", "price"],
    },
    "orders": {
        "file": "orders.csv",
        "columns": ["order_id", "customer_id", "order_date", "total_amount"],
    },
    "order_items": {
        "file": "order_items.csv",
        "columns": ["order_item_id", "order_id", "product_id", "qty", "unit_price"],
    },
    "reviews": {
        "file": "reviews.csv",
        "columns": ["review_id", "product_id", "customer_id", "rating", "comment"],
    },
}


def load_csv_rows(csv_path: Path, columns: list[str]) -> list[tuple]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing required CSV file: {csv_path}")
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [tuple(row[col] for col in columns) for row in reader]


def insert_rows(conn: sqlite3.Connection, table: str, columns: list[str], rows: list[tuple]):
    if not rows:
        return
    placeholders = ", ".join(["?"] * len(columns))
    column_list = ", ".join(columns)
    sql = f"INSERT INTO {table} ({column_list}) VALUES ({placeholders})"
    conn.executemany(sql, rows)


def main() -> None:
    base_path = Path(__file__).parent
    db_path = base_path / DB_NAME

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")

    schema_path = base_path / "schema.sql"
    if not schema_path.exists():
        raise FileNotFoundError("schema.sql not found")

    with schema_path.open(encoding="utf-8") as schema_file:
        conn.executescript(schema_file.read())

    try:
        for table, config in CSV_CONFIG.items():
            csv_path = base_path / config["file"]
            rows = load_csv_rows(csv_path, config["columns"])
            insert_rows(conn, table, config["columns"], rows)
        conn.commit()
    finally:
        conn.close()

    print(f"Created SQLite database at {db_path}")


if __name__ == "__main__":
    main()
