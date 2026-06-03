"""
DAY 1 — Live NAV Fetch from mfapi.in
Fetches real-time NAV data for 6 key funds and saves as CSV.
"""

import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

# ─── CONFIG ───────────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FUNDS_TO_FETCH = {
    "HDFC Top 100 Direct":  125497,
    "SBI Bluechip Regular": 119551,
    "ICICI Bluechip":       120503,
    "Nippon Large Cap":     118632,
    "Axis Bluechip":        119092,
    "Kotak Bluechip":       120841,
}

BASE_URL = "https://api.mfapi.in/mf/{}"

# ─── FETCH FUNCTION ───────────────────────────────────────────────────────────
def fetch_nav(amfi_code, fund_name):
    url = BASE_URL.format(amfi_code)
    print(f"  Fetching: {fund_name} (code: {amfi_code}) ... ", end="")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        nav_records = data.get("data", [])
        meta        = data.get("meta", {})

        df = pd.DataFrame(nav_records)
        df.rename(columns={"nav": "nav_value"}, inplace=True)
        df["amfi_code"]   = amfi_code
        df["fund_name"]   = fund_name
        df["scheme_name"] = meta.get("scheme_name", "")
        df["fund_house"]  = meta.get("fund_house", "")

        # API returns date as DD-MM-YYYY
        df["date"]      = pd.to_datetime(df["date"], format="%d-%m-%Y")
        df["nav_value"] = pd.to_numeric(df["nav_value"], errors="coerce")

        df.sort_values("date", inplace=True)
        df.reset_index(drop=True, inplace=True)

        print(f"✅ {len(df)} records | Latest NAV: ₹{df['nav_value'].iloc[-1]:.4f} on {df['date'].iloc[-1].date()}")
        return df

    except requests.exceptions.ConnectionError:
        print("❌ Network error — check internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


# ─── MAIN ─────────────────────────────────────────────────────────────────────
print("=" * 60)
print("LIVE NAV FETCH — mfapi.in")
print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 60)

all_frames = []

for fund_name, amfi_code in FUNDS_TO_FETCH.items():
    df = fetch_nav(amfi_code, fund_name)
    if df is not None:
        all_frames.append(df)
        safe_name = fund_name.lower().replace(" ", "_")
        out_path  = OUTPUT_DIR / f"live_nav_{amfi_code}_{safe_name}.csv"
        df.to_csv(out_path, index=False)

if all_frames:
    combined      = pd.concat(all_frames, ignore_index=True)
    combined_path = OUTPUT_DIR / "live_nav_all_funds.csv"
    combined.to_csv(combined_path, index=False)

    print(f"\n📊 Summary:")
    print(f"  Funds fetched  : {len(all_frames)}")
    print(f"  Total NAV rows : {len(combined):,}")
    print(f"  Saved to       : {combined_path}")

    print(f"\n  Latest NAVs:")
    latest = combined.groupby("fund_name").last()[["date", "nav_value"]].reset_index()
    print(latest.to_string(index=False))
else:
    print("\n⚠️  No data fetched. Check your internet connection.")

print("\n✅ Live NAV fetch complete!")