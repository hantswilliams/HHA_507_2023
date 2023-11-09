from faker import Faker
import pandas as pd
import numpy as np

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

fake = Faker()

# Define the number of samples we want
num_samples = 1000

# Generate fake data for each field
data = {
    'Age': [fake.random_int(min=18, max=90) for _ in range(num_samples)],
    'BMI': [fake.random_number(digits=2, fix_len=False) for _ in range(num_samples)],
    'Blood Pressure': [fake.random_int(min=80, max=180) for _ in range(num_samples)],
    'Smoking Status': [fake.random_element(elements=(0, 1)) for _ in range(num_samples)],
    'Disease Presence': [fake.random_element(elements=(0, 1)) for _ in range(num_samples)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Separate the features (X) and the target variable (y)
X = df.drop('Disease Presence', axis=1)
y = df['Disease Presence']



# Split the data into training and a temporary set (combining what will be validation and test later)
# We reserve 80% of the data for training and the remaining 20% for the temporary set.
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)

# Further split the temporary set into validation and test sets
# Since we want a 10% validation and 10% test set of the original data, and we have already reserved 20%,
# we split the temporary set in half to get 10% for validation and 10% for the test set.
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# The sizes of each dataset after splitting
train_size = X_train.shape[0]
val_size = X_val.shape[0]
test_size = X_test.shape[0]

train_size, val_size, test_size

