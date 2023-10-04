import pandas as pd 
import statsmodels.api as sm
import matplotlib.pyplot as plt

#### load in dataset for cleaning purposes

# load in dataset
df = pd.read_csv('WK5/examples/data/cms-hospital-provider-costs/Hospital_Cost_Report_2019.csv')

df.columns

## vars of interest: Number of Beds, FTE - Employees on Payroll, Patient Revenue, Outpatient Revenue
df = df[['Number of Beds', 'FTE - Employees on Payroll', 'Inpatient Revenue', 'Outpatient Revenue']]

# Remove any row with missing data
df = df.dropna()

# lets remove outliers, greater then 3 SDs from the mean
df = df[(df['Number of Beds'] - df['Number of Beds'].mean()) / df['Number of Beds'].std() < 3]
df = df[(df['FTE - Employees on Payroll'] - df['FTE - Employees on Payroll'].mean()) / df['FTE - Employees on Payroll'].std() < 3]
df = df[(df['Inpatient Revenue'] - df['Inpatient Revenue'].mean()) / df['Inpatient Revenue'].std() < 3]
df = df[(df['Outpatient Revenue'] - df['Outpatient Revenue'].mean()) / df['Outpatient Revenue'].std() < 3]

df.head(20)

## save 
df.to_csv('WK5/examples/data/cms-hospital-provider-costs/Hospital_Cost_Report_2019_small.csv')

################################################################
################################################################


# Define the dependent and independent variables
X = df['Number of Beds']
y = df['FTE - Employees on Payroll']


# Add a constant to the independent variable (required for the statsmodels regression model)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression
print(model.summary())

plt.scatter(df['Number of Beds'], df['FTE - Employees on Payroll'], label='Data Points')
plt.plot(df['Number of Beds'], model.predict(X), color='blue', label='Regression Line')
plt.xlabel('Number of Beds')
plt.ylabel('FTE - Employees on Payroll')
plt.title('Relationship between Number of Beds and Employees on Payroll')
plt.legend()
plt.show()