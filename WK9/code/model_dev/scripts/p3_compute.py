import pandas as pd
import pickle
import joblib


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix

from sklearn.dummy import DummyClassifier

from xgboost import XGBClassifier, XGBRegressor

import shap
import lime
from lime import lime_tabular

# Import the clean random sample of 10k data
df = pd.read_csv('WK9/code/model_dev/data/processed/crime_data_100k.csv')
len(df)

# drop rows with missing values
df.dropna(inplace=True)
len(df)

# Define the features and the target variable
X = df.drop('vict_sex', axis=1)  # Features (all columns except 'arrest')
y = df['vict_sex']               # Target variable (arrest)

# Initialize the StandardScaler
scaler = StandardScaler()
scaler.fit(X) # Fit the scaler to the features
pickle.dump(scaler, open('WK9/code/model_dev/models/scaler_100k.sav', 'wb')) # Save the scaler for later use

# Fit the scaler to the features and transform
X_scaled = scaler.transform(X)

# Split the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Check the size of each set
(X_train.shape, X_val.shape, X_test.shape)

# Pkle the X_train for later use in explanation
pickle.dump(X_train, open('WK9/code/model_dev/models/X_train_100k.sav', 'wb'))
# Pkle X.columns for later use in explanation
pickle.dump(X.columns, open('WK9/code/model_dev/models/X_columns_100k.sav', 'wb'))



##### Create a baseline model using DummyClassifier
# Initialize the DummyClassifier
dummy = DummyClassifier(strategy='most_frequent')
# Train the model on the training set
dummy.fit(X_train, y_train)
dummy_acc = dummy.score(X_val, y_val)



##### Create a Logistic Regression model
# Initialize the Logistic Regression model
log_reg = LogisticRegression()
# Train the model on the training set
log_reg.fit(X_train, y_train)
# Predict on the validation set
y_val_pred = log_reg.predict(X_val)
# Evaluate the model
log_reg_acc = log_reg.score(X_val, y_val)
log_reg_mse = mean_squared_error(y_val, y_val_pred)
log_reg_r2 = r2_score(y_val, y_val_pred)
# Print confusion matrix
print(confusion_matrix(y_val, y_val_pred))
# Display the classification report
print(classification_report(y_val, y_val_pred))
# Print the results
print('Baseline accuracy:', dummy_acc)
print('Logistic Regression accuracy:', log_reg_acc)
print('Logistic Regression MSE:', log_reg_mse)
print('Logistic Regression R2:', log_reg_r2)




####### Now lets use a different model, XGBoost
# Initialize the XGBoost classifier
xgboost = XGBClassifier()
# Train the model on the training set
xgboost.fit(X_train, y_train)
# Predict on the validation set
y_val_pred = xgboost.predict(X_val)
# Evaluate the model
xgboost_acc = xgboost.score(X_val, y_val)
xgboost_mse = mean_squared_error(y_val, y_val_pred)
xgboost_r2 = r2_score(y_val, y_val_pred)
# Print confusion matrix
print(confusion_matrix(y_val, y_val_pred))
# Display the classification report
print(classification_report(y_val, y_val_pred))
# Print the results
print('Baseline accuracy:', dummy_acc)
print('Logistic Regression accuracy:', log_reg_acc)
print('Logistic Regression MSE:', log_reg_mse)
print('Logistic Regression R2:', log_reg_r2)
print('XGBoost accuracy:', xgboost_acc)
print('XGBoost MSE:', xgboost_mse)
print('XGBoost R2:', xgboost_r2)



### now lets perform hyperparameter tuning on XGBoost
# Define the grid of hyperparameters
param_grid = {
    # there are 3 hyperparameters we want to tune:
    # and each hyperparameter has a list of values we want to try that need to be the same length
    # across all hyperparameters
    'learning_rate': [0.1, 0.01, 0.001], # learning rate is the step size shrinkage used to prevent overfitting
    'n_estimators': [100, 200, 300], # number of trees
    'max_depth': [3, 4, 5], # maximum depth of each tree
}

# Initialize the XGBoost classifier
xgboost = XGBClassifier()
# Initialize GridSearch
grid_search = GridSearchCV(estimator=xgboost, param_grid=param_grid, cv=3, n_jobs=-1)
# Fit the estimator
grid_search.fit(X_train, y_train)
# Predict on the validation set
y_val_pred = grid_search.predict(X_val)
# Evaluate the model
## Create dataframe of the actual and predicted values
df_results = pd.DataFrame({'actual': y_val, 'predicted': y_val_pred})
grid_search_acc = grid_search.score(X_val, y_val)
grid_search_mse = mean_squared_error(y_val, y_val_pred)
grid_search_r2 = r2_score(y_val, y_val_pred)
# Print confusion matrix
print(confusion_matrix(y_val, y_val_pred))
# Display the classification report
print(classification_report(y_val, y_val_pred))
# Print the results
print('Baseline accuracy:', dummy_acc)
print('Logistic Regression accuracy:', log_reg_acc)
print('XGBoost Model 1 accuracy:', xgboost_acc)
print('XGBoost Model 2 accuracy:', grid_search_acc)



# Print the best parameters and the best score
print(grid_search.best_params_)
print(grid_search.best_score_)



### now lets use the best parameters to train a new model
# Initialize the XGBoost classifier
xgboost = XGBClassifier(learning_rate=0.1, max_depth=5, n_estimators=200)
# Train the model on the training set
xgboost.fit(X_train, y_train)
# Predict on the test set
y_test_pred = xgboost.predict(X_test)
# Evaluate the model
xgboost_acc = xgboost.score(X_test, y_test)





####### EXPLORATION 
#### feature importance with SHAP
explainer = shap.TreeExplainer(xgboost)
explanation = explainer(X_test)
shape_vlaues = explanation.values
shap.summary_plot(explanation, X_test, plot_type="bar")

##### feature importance with LIME
explainer = lime_tabular.LimeTabularExplainer(
    training_data=X_train,
    feature_names=X.columns,
    class_names=['female', 'male'],
    mode='classification',
)

# Pick the observation in the validation set for which explanation is required
observation_1 = 20
# Get the explanation for Logistic Regression and show the prediction
exp = explainer.explain_instance(X_val[observation_1], xgboost.predict_proba, num_features=9)
exp.save_to_file('WK9/code/model_dev/models/observation_1.html')

## save the model
pickle.dump(xgboost, open('WK9/code/model_dev/models/xgboost_100k.sav', 'wb'))







