library(ggplot2)
library(lmtest)

df = read.csv('WK5/examples/data/cms-hospital-provider-costs/Hospital_Cost_Report_2019_small.csv')

model <- lm(df$FTE...Employees.on.Payroll ~ df$Number.of.Beds)
summary(model)

ggplot(df, aes(x = df$Number.of.Beds, y = df$FTE...Employees.on.Payroll)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "blue") +
  theme_minimal()