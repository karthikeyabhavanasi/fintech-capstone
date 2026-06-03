# Data Dictionary

## Source Reference

All datasets are provided as part of the Bluestock Mutual Fund Analytics Capstone Project.

---

# 01_fund_master.csv

| Column             | Data Type | Business Definition             |
| ------------------ | --------- | ------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier   |
| fund_house         | Text      | Mutual fund company name        |
| scheme_name        | Text      | Mutual fund scheme name         |
| category           | Text      | Broad fund category             |
| sub_category       | Text      | Specific fund category          |
| plan               | Text      | Direct or Regular plan          |
| launch_date        | Date      | Scheme launch date              |
| benchmark          | Text      | Benchmark index                 |
| expense_ratio_pct  | Float     | Annual expense ratio (%)        |
| exit_load_pct      | Float     | Exit load charged on redemption |
| min_sip_amount     | Integer   | Minimum SIP investment amount   |
| min_lumpsum_amount | Integer   | Minimum lump sum investment     |
| fund_manager       | Text      | Fund manager name               |
| risk_category      | Text      | Risk classification             |
| sebi_category_code | Text      | SEBI category code              |

---

# 02_nav_history.csv

| Column    | Data Type | Business Definition |
| --------- | --------- | ------------------- |
| amfi_code | Integer   | Scheme identifier   |
| date      | Date      | NAV date            |
| nav       | Float     | Net Asset Value     |

---

# 03_aum_by_fund_house.csv

| Column         | Data Type | Business Definition       |
| -------------- | --------- | ------------------------- |
| date           | Date      | Reporting date            |
| fund_house     | Text      | Asset management company  |
| aum_lakh_crore | Float     | AUM in lakh crore         |
| aum_crore      | Float     | AUM in crore              |
| num_schemes    | Integer   | Number of schemes managed |

---

# 04_monthly_sip_inflows.csv

| Column                    | Data Type | Business Definition              |
| ------------------------- | --------- | -------------------------------- |
| month                     | Date      | Reporting month                  |
| sip_inflow_crore          | Float     | SIP inflow amount                |
| active_sip_accounts_crore | Float     | Active SIP accounts              |
| new_sip_accounts_lakh     | Float     | New SIP registrations            |
| sip_aum_lakh_crore        | Float     | SIP assets under management      |
| yoy_growth_pct            | Float     | Year-over-year growth percentage |

---

# 05_category_inflows.csv

| Column           | Data Type | Business Definition |
| ---------------- | --------- | ------------------- |
| month            | Date      | Reporting month     |
| category         | Text      | Fund category       |
| net_inflow_crore | Float     | Net inflow amount   |

---

# 06_industry_folio_count.csv

| Column              | Data Type | Business Definition   |
| ------------------- | --------- | --------------------- |
| month               | Date      | Reporting month       |
| total_folios_crore  | Float     | Total investor folios |
| equity_folios_crore | Float     | Equity folios         |
| debt_folios_crore   | Float     | Debt folios           |
| hybrid_folios_crore | Float     | Hybrid folios         |
| others_folios_crore | Float     | Other folios          |

---

# 07_scheme_performance.csv

| Column             | Data Type | Business Definition           |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Scheme identifier             |
| scheme_name        | Text      | Scheme name                   |
| fund_house         | Text      | Fund house                    |
| category           | Text      | Fund category                 |
| plan               | Text      | Direct or Regular             |
| return_1yr_pct     | Float     | 1-year return                 |
| return_3yr_pct     | Float     | 3-year return                 |
| return_5yr_pct     | Float     | 5-year return                 |
| benchmark_3yr_pct  | Float     | Benchmark 3-year return       |
| alpha              | Float     | Alpha performance metric      |
| beta               | Float     | Beta volatility metric        |
| sharpe_ratio       | Float     | Risk-adjusted return metric   |
| sortino_ratio      | Float     | Downside risk-adjusted return |
| std_dev_ann_pct    | Float     | Annualized standard deviation |
| max_drawdown_pct   | Float     | Maximum decline from peak     |
| aum_crore          | Float     | Assets under management       |
| expense_ratio_pct  | Float     | Expense ratio                 |
| morningstar_rating | Integer   | Morningstar rating            |
| risk_grade         | Text      | Risk level                    |

---

# 08_investor_transactions.csv

| Column             | Data Type | Business Definition            |
| ------------------ | --------- | ------------------------------ |
| investor_id        | Text      | Unique investor ID             |
| transaction_date   | Date      | Transaction date               |
| amfi_code          | Integer   | Scheme identifier              |
| transaction_type   | Text      | SIP, Lumpsum or Redemption     |
| amount_inr         | Float     | Transaction amount             |
| state              | Text      | Investor state                 |
| city               | Text      | Investor city                  |
| city_tier          | Text      | T30 or B30 city classification |
| age_group          | Text      | Investor age category          |
| gender             | Text      | Investor gender                |
| annual_income_lakh | Float     | Annual income                  |
| payment_mode       | Text      | Payment channel                |
| kyc_status         | Text      | KYC verification status        |

---

# 09_portfolio_holdings.csv

| Column            | Data Type | Business Definition         |
| ----------------- | --------- | --------------------------- |
| amfi_code         | Integer   | Scheme identifier           |
| stock_symbol      | Text      | Stock ticker                |
| stock_name        | Text      | Company name                |
| sector            | Text      | Industry sector             |
| weight_pct        | Float     | Portfolio allocation weight |
| market_value_cr   | Float     | Market value in crore       |
| current_price_inr | Float     | Current stock price         |
| portfolio_date    | Date      | Portfolio reporting date    |

---

# 10_benchmark_indices.csv

| Column      | Data Type | Business Definition  |
| ----------- | --------- | -------------------- |
| date        | Date      | Index date           |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Closing index value  |
