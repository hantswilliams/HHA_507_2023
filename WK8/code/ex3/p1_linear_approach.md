# ML regression example with diabetes data and SciKit-Learn

1. Load the dataset into a pandas DataFrame.
2. Perform exploratory data analysis to understand the data.
3. Preprocess the data, handling missing values if necessary and scaling features if needed.
4. Split the data into training, validation, and testing sets.
5. Train a machine learning model using the training set.
6. Tune the model using the validation set.
7. Evaluate the model using the testing set.
8. Discuss potential next steps depending on the evaluation results.


## 1. Load the dataset into a pandas DataFrame.

```python

import pandas as pd

# Load the dataset
file_path = 'diabetes.csv'
diabetes_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
diabetes_data.head()

```

```text

OUTPUT: 

   HighBP  HighChol  CholCheck  BMI  Smoker  Stroke  HeartDiseaseorAttack  \
0       1         1          1   40       1       0                     0   
1       0         0          0   25       1       0                     0   
2       1         1          1   28       0       0                     0   
3       1         0          1   27       0       0                     0   
4       1         1          1   24       0       0                     0   

   PhysActivity  Fruits  Veggies  ...  NoDocbcCost  GenHlth  MentHlth  \
0             0       0        1  ...            0        5        18   
1             1       0        0  ...            1        3         0   
2             0       1        0  ...            1        5        30   
3             1       1        1  ...            0        2         0   
4             1       1        1  ...            0        2         3   

   PhysHlth  DiffWalk  Sex  Age  Education  Income  Diabetes_binary  
0        15         1    0    9          4       3                0  
1         0         0    0    7          6       1                0  
2        30         1    0    9          4       8                0  
3         0         0    0   11          3       6                0  
4         0         0    0   11          5       4                0  

[5 rows x 22 columns]

```

*Interpretation*: 

- The dataset contains several columns that are likely to be risk factors or indicators of diabetes.
- The `BMI` column, which represents Body Mass Index, is what we will predict. In this context, it's treated as a continuous variable, suggesting a regression task.
- The `Diabetes_binary` column appears to be a binary target variable indicating the presence or absence of diabetes, which would be used for a classification task.
- There are other health-related variables as well, such as `HighBP` for high blood pressure, `HighChol` for high cholesterol, `Smoker`, `Stroke`, and `HeartDiseaseorAttack`, among others.

---

Before proceeding with the machine learning steps, we would typically conduct an exploratory data analysis to check for missing values, understand the distribution of variables, and perform feature selection if necessary. 

The next steps are:

1. Preprocess the data: Check for missing values and standardize the features if necessary.
2. Split the data into training, validation, and testing sets.

Let's start by preprocessing the data. We'll check for missing values first. If there are any, we'll decide how to handle them based on the context and amount. Then we'll proceed with scaling the features, which is an important step before training many types of machine learning models.


```python
# Check for missing values in the dataset
missing_values = diabetes_data.isnull().sum()

# Output the number of missing values per column
missing_values[missing_values > 0]

```

```text
Series([], dtype: int64)

```


---


The dataset does not have any missing values, which simplifies the preprocessing step.

Next, we will scale the features. Feature scaling is a method used to standardize the range of independent variables or features of data. Since the ranges of values for the features in the dataset can vary widely, some machine learning algorithms can benefit from feature scaling to ensure that no variable dominates the model due to its scale.

We will:

1. Separate the features (X) from the target variable (y), which in this case is `BMI`.

2. Scale the features using standardization (which gives the data the properties of a standard normal distribution with \(\mu = 0\) and \(\sigma = 1\)).

3. Split the dataset into training (70%), validation (15%), and testing (15%) sets.

Let's proceed with these steps.

```python

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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


```

```text

((177576, 21), (38052, 21), (38052, 21))


```


---

The data has been successfully scaled and split into training, validation, and testing sets. Here are the sizes of each set:

- Training set: 177,576 samples
- Validation set: 38,052 samples
- Testing set: 38,052 samples

The next steps in the machine learning workflow will be to:

1. Train a regression model using the training set.
2. Tune the model using the validation set.
3. Evaluate the model using the testing set.

Given that our target variable `BMI` is continuous, we'll use a regression model. A good starting point is to use a simple model like Linear Regression to establish a baseline performance. 

Let's proceed to train the Linear Regression model.

```python

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

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


```

```text
RESULT:

(38.38881932645651, 0.13709682435446557)


```



The Linear Regression model has been trained and evaluated on the validation set. Here are the performance metrics:

- Mean Squared Error (MSE) on the validation set: \( 38.39 \)
- \( R^2 \) score on the validation set: \( 0.137 \)

The MSE indicates on average how much the model's predictions deviate from the actual values in terms of BMI. The \( R^2 \) score, which ranges from -1 to 1, describes the proportion of variance for BMI that's explained by the model. An \( R^2 \) score of \( 0.137 \) means that the model explains approximately 13.7% of the variance in BMI, which suggests there is a lot of room for improvement.

For further model improvement, we could consider the following steps:

1. Try more complex models that can capture non-linear relationships (e.g., Random Forest, Gradient Boosting).
2. Perform feature engineering to create more informative features.
3. Use regularization techniques to improve the model's generalization.

