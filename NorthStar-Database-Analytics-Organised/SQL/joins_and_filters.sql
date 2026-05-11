-- SQL Joins and Filtering Examples

SELECT j.journey_id,
       j.city_zone,
       j.delivery_status,
       c.customer_type,
       j.delay_minutes
FROM journeys j
JOIN customers c
ON j.customer_id = c.customer_id
WHERE j.delivery_status IN ('Delayed', 'Failed')
ORDER BY j.delay_minutes DESC;
