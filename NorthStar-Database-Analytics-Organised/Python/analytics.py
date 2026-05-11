import pandas as pd

df = pd.read_csv("../Data/sample_northstar_data.csv")
df["profit"] = df["revenue"] - df["cost"]

zone_summary = df.groupby("city_zone").agg(
    total_journeys=("journey_id", "count"),
    avg_delay=("delay_minutes", "mean"),
    total_profit=("profit", "sum")
).reset_index()

print("Operational performance by zone")
print(zone_summary)
