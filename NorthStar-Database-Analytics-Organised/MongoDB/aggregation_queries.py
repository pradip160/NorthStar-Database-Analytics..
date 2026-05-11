# MongoDB Aggregation Pipeline Examples

complaints_by_zone = [
    {"$match": {"delivery_status": {"$in": ["Delayed", "Failed"]}}},
    {"$group": {
        "_id": "$route.city_zone",
        "total_issues": {"$sum": 1},
        "avg_delay": {"$avg": "$route.delay_minutes"}
    }},
    {"$sort": {"total_issues": -1}}
]

profit_by_zone = [
    {"$group": {
        "_id": "$route.city_zone",
        "total_revenue": {"$sum": "$finance.revenue"},
        "total_cost": {"$sum": "$finance.cost"}
    }},
    {"$sort": {"total_revenue": -1}}
]

print("Aggregation pipeline examples ready.")
