library(readr)
library(dplyr)

df <- read_csv("../Data/sample_northstar_data.csv")

df <- df %>%
  mutate(profit = revenue - cost)

zone_summary <- df %>%
  group_by(city_zone) %>%
  summarise(
    total_journeys = n(),
    avg_delay = mean(delay_minutes),
    total_profit = sum(profit)
  )

print(zone_summary)
