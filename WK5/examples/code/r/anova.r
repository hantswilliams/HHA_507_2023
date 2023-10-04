
df = read.csv("sparcs_opioid_clean.csv")

model <- aov(overall_opioid ~ payer + rural_urban, data=df)

summary(model)

means_by_payer <- aggregate(overall_opioid ~ payer, data=df, FUN=mean)
print(means_by_payer)