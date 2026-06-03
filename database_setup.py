import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data/bluestock_mf.db")
DB_PATH.parent.mkdir(exist_ok=True)

print("=" * 50)
print("DAY 2 — SQLITE DATABASE SETUP")
print("=" * 50)

conn = sqlite3.connect(DB_PATH)

# ─── CREATE SCHEMA ────────────────────────────────
print("\nCreating tables from schema.sql...")
with open("sql/schema.sql", "r") as f:
    schema = f.read()
conn.executescript(schema)
conn.commit()
print("✅ All tables created")

# ─── LOAD DATA ────────────────────────────────────
print("\nLoading data into tables...")

# dim_fund
df = pd.read_csv("data/raw/01_fund_master.csv")
df[["amfi_code","fund_house","scheme_name",
    "category","sub_category","plan"]].to_sql(
    "dim_fund", conn, if_exists="replace", index=False)
print(f"  ✅ dim_fund           — {len(df)} rows")

# fact_nav
df = pd.read_csv("data/processed/nav_history_clean.csv")
df.rename(columns={"date": "nav_date"}, inplace=True)
df[["amfi_code","nav_date","nav"]].to_sql(
    "fact_nav", conn, if_exists="replace", index=False)
print(f"  ✅ fact_nav           — {len(df):,} rows")

# fact_transactions
df = pd.read_csv("data/processed/investor_transactions_clean.csv")
df[["investor_id","amfi_code","transaction_date",
    "transaction_type","amount_inr"]].to_sql(
    "fact_transactions", conn, if_exists="replace", index=False)
print(f"  ✅ fact_transactions  — {len(df):,} rows")

# fact_performance
df = pd.read_csv("data/processed/scheme_performance_clean.csv")
df[["amfi_code","return_1yr_pct","return_3yr_pct",
    "return_5yr_pct","expense_ratio_pct"]].to_sql(
    "fact_performance", conn, if_exists="replace", index=False)
print(f"  ✅ fact_performance   — {len(df)} rows")

# fact_aum
df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
df[["fund_house","aum_crore","date"]].to_sql(
    "fact_aum", conn, if_exists="replace", index=False)
print(f"  ✅ fact_aum           — {len(df)} rows")

# ─── VERIFY ROW COUNTS ────────────────────────────
print("\nVerifying row counts...")
tables = ["dim_fund","fact_nav","fact_transactions",
          "fact_performance","fact_aum"]
for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}", conn
    )["cnt"][0]
    print(f"  {table:25s} → {count:,} rows")

conn.close()
print("\n✅ Day 2 database setup complete!")
print("⚠️  Never push bluestock_mf.db to GitHub!")