# MongoDB CRUD Operations using PyMongo

example_journey = {
    "journey_id": "J00001",
    "customer": {
        "customer_id": "C0001",
        "customer_type": "Business"
    },
    "route": {
        "city_zone": "Central",
        "delay_minutes": 25
    },
    "delivery_status": "Delayed"
}

# CREATE
# journeys.insert_one(example_journey)

# READ
# journeys.find({"delivery_status": "Delayed"})

# UPDATE
# journeys.update_one(
#     {"journey_id": "J00001"},
#     {"$set": {"delivery_status": "Completed"}}
# )

# DELETE
# journeys.delete_one({"journey_id": "TEST_RECORD"})

print("CRUD operation examples ready.")
