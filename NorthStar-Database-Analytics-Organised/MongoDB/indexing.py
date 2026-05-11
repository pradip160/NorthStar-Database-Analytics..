# MongoDB Indexing and Query Optimisation

# journeys.create_index("journey_id")
# journeys.create_index("customer.customer_id")
# journeys.create_index("driver.driver_id")
# journeys.create_index("vehicle.vehicle_id")
# journeys.create_index("route.city_zone")
# journeys.create_index("delivery_status")
# journeys.create_index([("route.city_zone", 1), ("route.delay_minutes", -1)])

# Example explain plan:
# journeys.find({
#     "route.city_zone": "Central",
#     "delivery_status": "Delayed"
# }).explain("executionStats")

print("Indexing and explain-plan examples ready.")
