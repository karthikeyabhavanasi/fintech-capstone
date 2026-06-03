import pandas as pd

print("Loading nav_history.csv...")

nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort by AMFI code and date
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicate rows
nav = nav.drop_duplicates()

# Forward fill missing NAV values
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

print("Final Shape:", nav.shape)

# Save cleaned file
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("✅ nav_history_clean.csv saved")
print("\nLoading investor_transactions.csv...")

txn = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date format
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# Standardize transaction type
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

# Check valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]

txn = txn[
    txn["transaction_type"].isin(valid_types)
]

# Amount must be positive
txn = txn[
    txn["amount_inr"] > 0
]

# Check KYC values
print("\nKYC Status Values:")
print(txn["kyc_status"].unique())

print("Final Shape:", txn.shape)

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("✅ investor_transactions_clean.csv saved")
print("\nLoading scheme_performance.csv...")

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Convert to numeric
for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Remove rows with missing returns
perf = perf.dropna(
    subset=return_cols
)

# Check expense ratio range
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

print("Final Shape:", perf.shape)

print("\nExpense Ratio Range:")
print(
    perf["expense_ratio_pct"].min(),
    "to",
    perf["expense_ratio_pct"].max()
)

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("✅ scheme_performance_clean.csv saved")