This repository provides synthetic e-commerce CSV datasets, a SQLite schema, an ingestion script, and sample SQL queries so you can quickly stand up a demo database and explore shopper, product, order, and review analytics end-to-end.
Prompts
1.<img width="718" height="245" alt="Screenshot 2025-11-14 143713" src="https://github.com/user-attachments/assets/3a30effa-b9bc-48ad-a2d1-ade21f799cb5" />
2.<img width="774" height="306" alt="Screenshot 2025-11-14 143857" src="https://github.com/user-attachments/assets/a5091d23-1ab3-4eda-9308-898b5a4c22e9" />
3.<img width="679" height="290" alt="Screenshot 2025-11-14 144016" src="https://github.com/user-attachments/assets/8b0905b4-3575-4787-b50d-691c4e1bf4ce" />
4.<img width="696" height="272" alt="Screenshot 2025-11-14 144046" src="https://github.com/user-attachments/assets/28545eb3-fad1-4808-942f-2f5eef14ead9" />
5.<img width="688" height="307" alt="Screenshot 2025-11-14 144121" src="https://github.com/user-attachments/assets/2d1068a9-012b-4393-beb4-63868ba0f5ab" />

# 🚀 Cursor E-Commerce Data Pipeline

*A lightweight, AI-assisted SDLC mini-project built entirely in Cursor IDE.*

## 🌸 Project Overview

This project generates a synthetic e-commerce dataset, ingests it into a SQLite database, and runs analytical SQL queries — including an advanced composite multi-CTE query that simulates real-world BI reporting.

## 📦 Key Deliverables

* Synthetic e-commerce dataset (5 CSV files)
* SQLite schema + automated ingestion script
* Analytical SQL queries
* Advanced composite analytics
* Clean GitHub repository with proper structure
* Fully reproducible workflow

## 📂 Repository Structure

* customers.csv
* products.csv
* orders.csv
* order_items.csv
* reviews.csv
* schema.sql
* ingest_to_sqlite.py
* sample_queries.sql
* run_queries.py
* README.md

## 🔧 Features

### Synthetic Dataset

* Five CSV files
* 100% referential integrity
* Consistent products, customers, orders, items, reviews

### SQLite Ingestion

* Automated creation of ecom.db
* Schema generated from schema.sql
* Bulk insertion from CSV scripts

### Analytics Suite

* Top customers by spend
* Best-selling products
* Monthly revenue trends
* Monthly composite analytics using window functions + CTEs

### Developer Hygiene

* ecom.db ignored using .gitignore
* CSVs are source of truth
* Modular scripts for clarity and extensibility

## ▶️ How to Run

### Step 1: Ingest the database

python3 ingest_to_sqlite.py

### Step 2: Run all queries

python3 run_queries.py

## 📊 Composite Analytics Query

The advanced SQL query calculates, for each month:

* Total revenue
* Number of orders
* Top-selling product
* Product name
* Average rating for that month’s top product

Built using:

* Common Table Expressions
* Window functions
* Multi-table joins
* Deterministic tie-breaking logic

## 🌐 GitHub Repository

[https://github.com/Sukruthgowdams/Diligent.git](https://github.com/Sukruthgowdams/Diligent.git)

## 💡 Notes

* Database file (ecom.db) is intentionally excluded from Git tracking.
* All computations run offline.
* CSVs are the primary data source for ingestion.

## ✨ Author

**Sukruth MS**
Reva University
B.Tech — CSIT
