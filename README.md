# 🏗️ Medallion Architecture Data Pipeline Challenge

Welcome to this hands-on coding exercise! In this challenge, you'll simulate building a simple data pipeline using the **Medallion Architecture** — a modern approach to organizing data in cloud data lakes.

You'll work through three transformation stages: **Bronze**, **Silver**, and **Gold**, each one representing a step closer to analytics-ready data.

Your goal is to create readable, maintainable code that processes raw data into a structured format. You're encouraged to use any framerwork or libraries you prefer, such as Pandas, PySpark, or Dask.

---

## 🚀 Objective

Your goal is to process raw input data across three layers:

1. **Bronze Layer – Ingest**  
   Load raw data from source files with minimal transformation. Think of this as your landing zone.

2. **Silver Layer – Clean & Enrich**  
   Standardize and clean the data. Fix data types, remove invalid values, and add useful metadata (e.g., ingestion timestamp, source info).

3. **Gold Layer – Final Output**  
   Combine and transform the cleaned data to produce an analytics-ready dataset — for example, by joining datasets or aggregating KPIs.

---

## 📁 Project Structure

```
medallion-architecture-challenge/
├── data_source/ # Raw data files (CSV/JSON)
├── datalake/
│ ├── bronze/ # Ingested raw data
│ ├── silver/ # Cleaned and enriched data
│ └── gold/   # Final, ready-to-use data
├── src/
│ ├── layers/
│ │ ├── bronze_layer.py # Bronze layer for raw data ingestion
│ │ ├── silver_layer.py # Silver layer for data cleaning and enrichment
│ │ ├── gold_layer.py   # Gold layer for final data transformation
│ │ └── utils/          # Add here your utility functions
│ └── main.py
├── requirements.txt
└── README.md
```

---

## 🧪 Data

You’ll find sample raw data in `data_source/`. This could include things like:

- User events
- Product metadata
- Transactions

Feel free to extend the data or simulate additional sources.

---

## 🛠️ How to Run

1. Install requirements:

```bash
python -m pip install -r requirements.txt
python ./src/main.py
```

# Add additional steps if needed in order to run the code.
```