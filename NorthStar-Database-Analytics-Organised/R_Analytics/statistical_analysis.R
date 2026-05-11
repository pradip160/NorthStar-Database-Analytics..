library(readr)

df <- read_csv("../Data/sample_northstar_data.csv")

print(summary(df$delay_minutes))
print(summary(df$revenue))
print(summary(df$cost))

correlation <- cor(df$delay_minutes, df$revenue)
print(paste("Correlation between delay and revenue:", correlation))
