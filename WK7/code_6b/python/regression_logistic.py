import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from statsmodels.stats.diagnostic import linear_rainbow
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import het_goldfeldquandt

# Sample data
data = {
    'Blood Pressure': [117, 130, 126, 113, 111, 116, 120, 120, 110, 115],
    'Blood Sugar': [80, 150, 140, 90, 85, 130, 140, 100, 90, 110],
    'Hospitalized': [1, 1, 1, 0, 0, 1, 1, 0, 0, 1]
}
df = pd.DataFrame(data)


# Fit the logistic regression model
X = df[['Blood Pressure', 'Blood Sugar']]
X = sm.add_constant(X)  # Adds a constant term to the predictor
y = df['Hospitalized']
model = sm.Logit(y, X)
results = model.fit()

# Print summary of the regression
print(results.summary())

# Predicted values
predicted = results.predict(X)
predicted_classes = [1 if x >= 0.5 else 0 for x in predicted]

# CHECKING ASSUMPTIONS

# Linearity of the logit
# Plot observed vs fitted values
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Hospitalized'], y=predicted)
plt.xlabel('Observed Values')
plt.ylabel('Fitted Values')
plt.title('Observed vs Fitted Values')
plt.plot([0, 1], [0, 1], color='red', linestyle='--')
plt.show()

# Assessing normality of residuals
residuals = results.resid_dev
W, p_value = shapiro(residuals)
print(f"Shapiro-Wilk Test: W={W}, p-value={p_value}")

# Plot Q-Q plot of residuals
plt.figure(figsize=(10, 6))
stats.probplot(residuals, plot=plt)
plt.title('Q-Q Plot of Residuals')
plt.show()

# Assessing homogeneity of variance of residuals
gq_test = het_goldfeldquandt(residuals, results.model.exog)
print(f"Goldfeld-Quandt Test: F-statistic={gq_test[0]}, p-value={gq_test[1]}")

# Plot residuals vs fitted values
plt.figure(figsize=(10, 6))
sns.scatterplot(x=predicted, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted Values')
plt.show()