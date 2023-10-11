## generating fake data

# Sample data frame (for demonstration purposes)
df <- data.frame(
  ID = 1:100,
  Blood_Glucose = c(
    rnorm(25, 150, 20),  # Diabetic & Overweight
    rnorm(25, 130, 15),  # Diabetic & Not Overweight
    rnorm(25, 100, 10),  # Non-diabetic & Overweight
    rnorm(25, 90, 7)     # Non-diabetic & Not Overweight
  ),
  Diabetic_Status = factor(rep(c('Diabetic', 'Non-diabetic'), each=50)),
  Weight_Status = factor(rep(c('Overweight', 'Not Overweight', 'Overweight', 
'Not Overweight'), each=25))
)


## checking for normality 

# Manually specify combinations
combinations <- list(
  list(Diabetic_Status = "Diabetic", Weight_Status = "Overweight"),
  list(Diabetic_Status = "Diabetic", Weight_Status = "Not Overweight"),
  list(Diabetic_Status = "Non-diabetic", Weight_Status = "Overweight"),
  list(Diabetic_Status = "Non-diabetic", Weight_Status = "Not Overweight")
)

# Apply the Shapiro-Wilk test to each combination
for (combination in combinations) {
  subset <- df[df$Diabetic_Status == combination$Diabetic_Status & df$Weight_Status == combination$Weight_Status, ]
  test_result <- shapiro.test(subset$Blood_Glucose)
  cat("Group (", combination$Diabetic_Status, ", ", combination$Weight_Status, "):\n", sep = "")
  cat("P-value from Shapiro-Wilk Test:", test_result$p.value, "\n\n")
}


## visualization 

# For demonstration purposes, let's use one of the subsets:
subset <- df[df$Diabetic_Status == "Diabetic" & df$Weight_Status == "Overweight", ]

# Histogram
hist(subset$Blood_Glucose, breaks=20, main="Histogram of Blood Glucose Levels", xlab="Blood Glucose Level", border="black", col="grey")

# Q-Q Plot
qqnorm(subset$Blood_Glucose, main="Q-Q Plot of Blood Glucose Levels")
qqline(subset$Blood_Glucose, col="blue")