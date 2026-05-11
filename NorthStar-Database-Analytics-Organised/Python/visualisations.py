import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Data/sample_northstar_data.csv")

zone_delay = df.groupby("city_zone")["delay_minutes"].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(zone_delay["city_zone"], zone_delay["delay_minutes"])
plt.xlabel("City Zone")
plt.ylabel("Average Delay Minutes")
plt.title("Average Delivery Delay by City Zone")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../Visualisations/delay_by_zone.png")
plt.show()
