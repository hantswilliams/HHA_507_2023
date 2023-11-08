from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from joblib import dump, load


import pandas as pd


####### Step 0 - non-ML step - Load and prepare the dataset ######
### splitting it into training, validation, and testing sets ###

# Load the dataset
file_path = 'WK8/code/ex1/diabetes.csv'
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



# Step 1: Create a baseline decision tree model without any hyperparameter tuning
baseline_dt_model = DecisionTreeRegressor(random_state=42)
baseline_dt_model.fit(X_train, y_train)
## get baseline model performance on validation set
y_val_pred_baseline = baseline_dt_model.predict(X_val)
mse_val_baseline = mean_squared_error(y_val, y_val_pred_baseline)
r2_val_baseline = r2_score(y_val, y_val_pred_baseline)
print("Baseline Decision Tree model performance on validation set: MSE = %0.4f, R2 = %0.4f" % (mse_val_baseline, r2_val_baseline))



#### Steps 

# Step 2: Manually adjust hyperparameters and evaluate the model
# Step 2a: Adjust the max_depth hyperparameter
# Adjust the max_depth to 5
dt_model_depth_5 = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_model_depth_5.fit(X_train, y_train)
y_val_pred_depth_5 = dt_model_depth_5.predict(X_val)
mse_val_depth_5 = mean_squared_error(y_val, y_val_pred_depth_5)
r2_val_depth_5 = r2_score(y_val, y_val_pred_depth_5)
print("Decision Tree model performance on validation set with max_depth = 5: MSE = %0.4f, R2 = %0.4f" % (mse_val_depth_5, r2_val_depth_5))

# Step 2b: Adjust the max_depth hyperparameter
# Adjust the max_depth to 10
dt_model_depth_10 = DecisionTreeRegressor(max_depth=10, random_state=42)
dt_model_depth_10.fit(X_train, y_train)
y_val_pred_depth_10 = dt_model_depth_10.predict(X_val)
mse_val_depth_10 = mean_squared_error(y_val, y_val_pred_depth_10)
r2_val_depth_10 = r2_score(y_val, y_val_pred_depth_10)
print("Decision Tree model performance on validation set with max_depth = 10: MSE = %0.4f, R2 = %0.4f" % (mse_val_depth_10, r2_val_depth_10))


# Output the results from the baseline model and the two manually adjusted models
print(f"""
      Baseline with no tuning: MSE = {mse_val_baseline:.4f}, R2 = {r2_val_baseline:.4f} 
      Decision Tree max_depth = 5: MSE = {mse_val_depth_5:.4f}, R2 = {r2_val_depth_5:.4f}
      Decision Tree max_depth = 10: MSE = {mse_val_depth_10:.4f}, R2 = {r2_val_depth_10:.4f}
""")




## Based on these results, the best model is the one with max_depth = 10
## so we will use this model to predict on the test set

# Step 3: Predict on the test set
y_test_pred_depth_10 = dt_model_depth_10.predict(X_test)
mse_test_depth_10 = mean_squared_error(y_test, y_test_pred_depth_10)
r2_test_depth_10 = r2_score(y_test, y_test_pred_depth_10)
print("Decision Tree model performance on test set with max_depth = 10: MSE = %0.4f, R2 = %0.4f" % (mse_test_depth_10, r2_test_depth_10))




### Save the model 
# Assuming `dt_model_depth_10` is your best model after evaluation
# Save the model to a file
model_filename = 'WK8/code/ex1/model/decision_tree_model.joblib'
dump(dt_model_depth_10, model_filename)


### Example of retrieving the model 
# Load the model from the file
best_model = load(model_filename)
productionData = X.sample(1)
productionData
y_test_pred_best_model = best_model.predict(productionData) # Use the loaded model to make predictions
print(y_test_pred_best_model)

