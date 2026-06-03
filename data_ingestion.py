"""
DAY 1 — Data Ingestion Script
Loads all 10 CSV files, prints shape/dtypes/head, and runs a data quality check.
"""

import pandas as pd
import os
from pathlib import Path

# ─── CONFIG ───────────────────────────────────────────────────────────────────
# Path to your raw CSV files
DATA_RAW = Path("data/raw")

CSV_FILES = {
    "fund_master":          "01_fund_master.csv",
    "nav_history":          "02_nav_history.csv",
    "aum_by_fund_house":    "03_aum_by_fund_house.csv",
    "monthly_sip_inflows":  "04_monthly_sip_inflows.csv",
    "category_inflows":     "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance":   "07_scheme_performance.csv",
    "investor_transactions":"08_investor_transactions.csv",
    "portfolio_holdings":   "09_portfolio_holdings.csv",
    "benchmark_indices":    "10_benchmark_indices.csv",
}

# ─── LOAD ALL CSVs ────────────────────────────────────────────────────────────
dataframes = {}

print("=" * 60)
print("LOADING ALL 10 CSV FILES")
print("=" * 60)

for name, filename in CSV_FILES.items():
    filepath = DATA_RAW / filename
    df = pd.read_csv(filepath)
    dataframes[name] = df

    print(f"\n📄 {filename}")
    print(f"   Shape      : {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"   Columns    : {list(df.columns)}")
    print(f"   Null count :\n{df.isnull().sum().to_string()}")
    print(f"   First 3 rows:\n{df.head(3).to_string()}")
    print("-" * 60)

# ─── DATA QUALITY CHECK ───────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

fund_master = dataframes["fund_master"]
nav_history = dataframes["nav_history"]

# 1. Unique values in fund_master
print("\n📊 Fund Master — Unique Values:")
print(f"  Fund houses    : {fund_master['fund_house'].nunique()} → {sorted(fund_master['fund_house'].unique())}")
print(f"  Categories     : {fund_master['category'].unique()}")
print(f"  Sub-categories : {fund_master['sub_category'].unique()}")
print(f"  Risk grades    : {fund_master['risk_category'].unique()}")
print(f"  Plan types     : {fund_master['plan'].unique()}")

# 2. AMFI Code Validation
master_codes  = set(fund_master["amfi_code"].unique())
nav_codes     = set(nav_history["amfi_code"].unique())
missing_codes = master_codes - nav_codes

print(f"\n✅ AMFI Code Validation:")
print(f"  Codes in fund_master : {len(master_codes)}")
print(f"  Codes in nav_history : {len(nav_codes)}")

if missing_codes:
    print(f"  ⚠️  Missing from nav_history: {missing_codes}")
else:
    print(f"  ✅ All codes matched successfully!")

# 3. NAV date range
nav_history["date"] = pd.to_datetime(nav_history["date"])
print(f"\n📅 NAV History:")
print(f"  Date range     : {nav_history['date'].min()} → {nav_history['date'].max()}")
print(f"  Total records  : {len(nav_history):,}")

# 4. Check for negative NAV
neg_nav = nav_history[nav_history["nav"] <= 0]
if len(neg_nav) > 0:
    print(f"  ⚠️  {len(neg_nav)} rows with zero or negative NAV!")
else:
    print(f"  ✅ No negative NAV values found.")

# 5. Investor transactions overview
txn = dataframes["investor_transactions"]
print(f"\n👥 Investor Transactions:")
print(f"  Transaction types : {txn['transaction_type'].unique()}")
print(f"  States covered    : {txn['state'].nunique()}")
print(f"  City tiers        : {txn['city_tier'].unique()}")

# ─── SAVE CLEAN COPIES ───────────────────────────────────────────────────────
processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

for name, df in dataframes.items():
    out_path = processed_dir / f"{name}_clean.csv"
    df.to_csv(out_path, index=False)
    print(f"  💾 Saved: {out_path}")

print("\n✅ Day 1 complete! All clean CSVs saved to data/processed/")
