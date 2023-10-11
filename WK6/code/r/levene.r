install.packages("lawstat")
library(lawstat)

# Levene's Test
result <- levene.test(df$Blood_Glucose, df$Weight_Status)
print(result)


# OR Levene's Test
result <- levene.test(df$Blood_Glucose, interaction(df$Weight_Status, df$Blood_Glucose))
print(result)

library(ggplot2)

# Box Plot
ggplot(df, aes(x=interaction(Weight_Status), y=Blood_Glucose)) + 
  geom_boxplot() + 
  labs(title="Box plot of Blood Glucose across Groups", x="Groups", y="Blood Glucose")

