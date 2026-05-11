library(readr)
library(ggplot2)
library(dplyr)

df <- read_csv("../Data/sample_northstar_data.csv")

zone_delay <- df %>%
  group_by(city_zone) %>%
  summarise(avg_delay = mean(delay_minutes))

ggplot(zone_delay, aes(x = city_zone, y = avg_delay)) +
  geom_col() +
  labs(
    title = "Average Delivery Delay by City Zone",
    x = "City Zone",
    y = "Average Delay Minutes"
  )
