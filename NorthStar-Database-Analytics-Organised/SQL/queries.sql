-- NorthStar SQL Queries

-- 1. Complaints or failed deliveries by city zone
SELECT city_zone, COUNT(*) AS total_failed
FROM journeys
WHERE delivery_status = 'Failed'
GROUP BY city_zone
ORDER BY total_failed DESC;

-- 2. Average delay by city zone
SELECT city_zone, ROUND(AVG(delay_minutes), 2) AS avg_delay
FROM journeys
GROUP BY city_zone
ORDER BY avg_delay DESC;

-- 3. Profitability by zone
SELECT city_zone,
       SUM(revenue) AS total_revenue,
       SUM(cost) AS total_cost,
       SUM(revenue - cost) AS total_profit
FROM journeys
GROUP BY city_zone
ORDER BY total_profit DESC;
