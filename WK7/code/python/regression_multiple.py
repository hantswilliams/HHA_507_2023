import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import linear_rainbow
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import het_goldfeldquandt


# Sample data
data = {
    'BMI': [24.679912, 34.186786, 30.577900, 28.377865, 21.074308, 26.647627, 27.125092, 25.554427, 18.919416, 20.280209],
    'Age': [25, 34, 30, 28, 21, 26, 27, 25, 18, 20],
    'Blood Pressure': [117.455103, 129.785142, 126.325654, 112.628953, 110.513102, 115.892390, 120.302129, 120.037400, 109.762577, 114.556229]
}
df = pd.DataFrame(data)

# Fit the regression model
X = df[['BMI', 'Age']]
X = sm.add_constant(X)  # Adds a constant term to the predictor
y = df['Blood Pressure']
model = sm.OLS(y, X)
results = model.fit()

# Print summary of the regression
print(results.summary())


residuals = results.resid
fitted = results.fittedvalues


##### CHECKING ASSUMPTIONS #####

# Checking multicollinearity using VIF
vif_data = pd.DataFrame()
vif_data['Variable'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print("\nVIF Data:")
print(vif_data)

### Assessing linearity of the relationship
stat, p_value = linear_rainbow(results)
print(f"Rainbow Test: stat={stat}, p-value={p_value}")

## A significant p-value indicates that the relationship is not linear.
# Plot observed vs fitted values
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Blood Pressure'], y=fitted)
plt.xlabel('Observed Values')
plt.ylabel('Fitted Values')
plt.title('Observed vs Fitted Values')
plt.plot([min(df['Blood Pressure']), max(df['Blood Pressure'])], [min(fitted), max(fitted)], color='red', linestyle='--')
plt.show()




### Assessing normality of the residuals
W, p_value = shapiro(residuals)
print(f"Shapiro-Wilk Test: W={W}, p-value={p_value}")

# Plot Q-Q plot of residuals
plt.figure(figsize=(10, 6))
stats.probplot(residuals, plot=plt)
plt.title('Q-Q Plot of Residuals')
plt.show()




##### Assessing the homogeneity of variance of the residuals
gq_test = het_goldfeldquandt(residuals, results.model.exog)
print(f"Goldfeld-Quandt Test: F-statistic={gq_test[0]}, p-value={gq_test[1]}")

# a significant p-value indicates heteroscedasticity, meaning that the variance of the 
# residuals is not constant across different levels of the independent variable(s).

# Plot residuals vs fitted values
plt.figure(figsize=(10, 6))
sns.scatterplot(x=fitted, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted Values')
plt.show()




