import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score


# Load the dataset
file_path = 'WK8/code/diabetes.csv'
diabetes_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
diabetes_data.head()

# Check for missing values in the dataset
missing_values = diabetes_data.isnull().sum()

# Output the number of missing values per column
missing_values[missing_values > 0]

# Define the features and the target variable
X = diabetes_data.drop('BMI', axis=1)  # Features (all columns except 'BMI')
y = diabetes_data['BMI']               # Target variable (BMI)

# Initialize the StandardScaler

"""
Data standardization is the process of rescaling the attributes so that they have mean as 0 and variance as 1.
The ultimate goal to perform standardization is to bring down all the features to a common scale without distorting the differences in the range of the values.
In sklearn.preprocessing.StandardScaler(), centering and scaling happens independently on each feature.
"""

scaler = StandardScaler()

# Fit the scaler to the features and transform
X_scaled = scaler.fit_transform(X)

# Split the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Check the size of each set
(X_train.shape, X_val.shape, X_test.shape)





#### Part 1. Generating BASELINE without any hyperparameter tuning
#### and using the training dataframe only

# Initialize the Linear Regression model
linear_reg = LinearRegression()

# Train the model on the training set
linear_reg.fit(X_train, y_train)

# Predict on the validation set
y_val_pred = linear_reg.predict(X_val)

# Calculate the performance metrics on the validation set
mse_val = mean_squared_error(y_val, y_val_pred)
r2_val = r2_score(y_val, y_val_pred)

(mse_val, r2_val)

## these numbers now become our baseline (mse_val and r2_val) to compare with other models 


###############################################################



#### Part 2. Now performing hyperparameter tuning 
####################

"""

For a simple leaner regression, there is only one hyperparameter to tune: the intercept.
Thus not much to tune here. 

"""

# Predict on the test set
y_test_pred = linear_reg.predict(X_test)

# Calculate the performance metrics on the test set
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)
(mse_test, r2_test)









####################


# Compare the performance metrics on the validation and test sets
(mse_val, mse_test)
(r2_val, r2_test)

# Compare the actual and predicted values for the first few rows of the test set
y_test_pred[:5]
y_test[:5]

df_compare = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
df_compare['delta'] = df_compare['Actual'] - df_compare['Predicted']

