This repository provides synthetic e-commerce CSV datasets, a SQLite schema, an ingestion script, and sample SQL queries so you can quickly stand up a demo database and explore shopper, product, order, and review analytics end-to-end.
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
