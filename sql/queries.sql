-- 1. Top 5 Funds by AUM

SELECT fund_house,
       MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;


-- 2. Average NAV per Fund

SELECT amfi_code,
       ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- 3. Monthly Average NAV

SELECT substr(nav_date,1,7) AS month,
       ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 4. Total Transactions

SELECT COUNT(*) AS total_transactions
FROM fact_transactions;


-- 5. Funds with Expense Ratio < 1%

SELECT amfi_code,
       expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 6. Total Transaction Amount by Type

SELECT transaction_type,
       SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 7. Average 3-Year Return

SELECT ROUND(AVG(return_3yr_pct),2)
AS avg_return_3yr
FROM fact_performance;


-- 8. Top 5 Funds by 5-Year Return

SELECT amfi_code,
       return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- 9. Fund Count by Category

SELECT category,
       COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;


-- 10. Average Expense Ratio

SELECT ROUND(AVG(expense_ratio_pct),2)
AS avg_expense_ratio
FROM fact_performance;