-- SQL Query Optimisation Examples

CREATE INDEX idx_journeys_city_zone ON journeys(city_zone);
CREATE INDEX idx_journeys_status ON journeys(delivery_status);
CREATE INDEX idx_journeys_customer ON journeys(customer_id);

EXPLAIN QUERY PLAN
SELECT city_zone, COUNT(*)
FROM journeys
WHERE delivery_status = 'Delayed'
GROUP BY city_zone;
