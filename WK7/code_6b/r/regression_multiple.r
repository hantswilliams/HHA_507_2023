install.packages("rms")

# Load libraries
library(ggplot2)
library(lmtest) # homogeneity of variances of the residuals, Breusch-Pagan test 
library(rms) # Harvey-Collier test for testing linearity.


# Sample data
BMI <- c(24.679912, 34.186786, 30.577900, 28.377865, 21.074308, 26.647627, 27.125092, 25.554427, 18.919416, 20.280209)
Age <- c(25, 34, 30, 28, 21, 26, 27, 25, 18, 20)
Blood_Pressure <- c(117.455103, 129.785142, 126.325654, 112.628953, 110.513102, 115.892390, 120.302129, 120.037400, 109.762577, 114.556229)
data <- data.frame(BMI, Age, Blood_Pressure)

# Fit the regression model
model <- lm(Blood_Pressure ~ BMI + Age + Gender, data)
summary(model)

# Calculate residuals and fitted values
residuals <- model$residuals
fitted <- model$fitted.values

# CHECKING ASSUMPTIONS

# Assessing linearity of the relationship
plot(fitted, residuals)
abline(h = 0, col = "red")
title("Residuals vs Fitted Values")
plot(data$Blood_Pressure, fitted)
abline(0, 1, col = "red")
title("Observed vs Fitted Values")

# Harvey-Collier test for linearity
hc_test <- harvtest(model)
print(hc_test)

# Assessing normality of residuals
shapiro.test(residuals)
qqnorm(residuals)
qqline(residuals)

# Assessing homogeneity of variance of residuals
bp_test <- bptest(model)
print(bp_test)