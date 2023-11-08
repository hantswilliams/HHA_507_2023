from xgboost import XGBRegressor

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

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
scaler = StandardScaler()

# Fit the scaler to the features and transform
X_scaled = scaler.fit_transform(X)

# Split the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Check the size of each set
(X_train.shape, X_val.shape, X_test.shape)















####################

# Initialize the XGBRegressor
xgboost_reg = XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)

# Train the model on the training set
xgboost_reg.fit(X_train, y_train)

# Predict on the validation set
y_val_pred_xgb = xgboost_reg.predict(X_val)

# Calculate the performance metrics on the validation set
mse_val_xgb = mean_squared_error(y_val, y_val_pred_xgb)
r2_val_xgb = r2_score(y_val, y_val_pred_xgb)

(mse_val_xgb, r2_val_xgb)








####################

# Predict on the test set
y_test_pred_xgb = xgboost_reg.predict(X_test)

# Calculate the performance metrics on the test set
mse_test_xgb = mean_squared_error(y_test, y_test_pred_xgb)
r2_test_xgb = r2_score(y_test, y_test_pred_xgb)

(mse_test_xgb, r2_test_xgb)




####################

# Compare the performance metrics on the validation and test sets
(mse_val_xgb, mse_test_xgb)
(r2_val_xgb, r2_test_xgb)

# Compare the actual and predicted values for the first few rows of the test set
df_compare = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred_xgb})
df_compare['delta'] = df_compare['Actual'] - df_compare['Predicted']
