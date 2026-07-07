-- Sales & Customer Data Analysis: SQL queries
-- Run against the `sales` table loaded via notebooks/01_cleaning_and_load.ipynb

-- 1. Top 5 products by total revenue
SELECT product, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 5;

-- 2. Monthly revenue trend
SELECT DATE_TRUNC('month', order_date) AS month, SUM(revenue) AS monthly_revenue
FROM sales
GROUP BY 1
ORDER BY 1;

-- 3. Revenue by region and category (joins-style aggregation)
SELECT region, category, SUM(revenue) AS revenue, COUNT(*) AS orders
FROM sales
GROUP BY region, category
ORDER BY region, revenue DESC;

-- 4. Top 10 customers by total spend
SELECT customer_id, SUM(revenue) AS total_spend, COUNT(*) AS orders
FROM sales
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT 10;

-- 5. Month-over-month revenue growth (window function)
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date) AS month, SUM(revenue) AS revenue
    FROM sales
    GROUP BY 1
)
SELECT month,
       revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
       ROUND(
         100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
         / NULLIF(LAG(revenue) OVER (ORDER BY month), 0), 2
       ) AS mom_growth_pct
FROM monthly
ORDER BY month;

-- 6. Rank products within each region by revenue (window function)
SELECT region, product, revenue_by_product,
       RANK() OVER (PARTITION BY region ORDER BY revenue_by_product DESC) AS rank_in_region
FROM (
    SELECT region, product, SUM(revenue) AS revenue_by_product
    FROM sales
    GROUP BY region, product
) t
ORDER BY region, rank_in_region;
