data = read.csv('')

contingency_table <- table(data$DME, data$HHA)
chi2_test <- chisq.test(contingency_table)
