# generating fake data

import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Set a seed for reproducibility
seed = 42
np.random.seed(seed)
Faker.seed(seed)

# Number of samples
n = 100

# Create a DataFrame
df = pd.DataFrame({
    'ID': [fake.uuid4() for _ in range(n)],
    'Blood Glucose': np.concatenate([
        np.random.normal(150, 20, int(n/4)),  # Diabetic & Overweight
        np.random.normal(130, 15, int(n/4)),  # Diabetic & Not Overweight
        np.random.normal(100, 10, int(n/4)),  # Non-diabetic & Overweight
        np.random.normal(90, 7, int(n/4))     # Non-diabetic & Not Overweight
    ]),
    'Diabetic Status': np.concatenate([
        ['Diabetic'] * int(n/2),
        ['Non-diabetic'] * int(n/2)
    ]),
    'Weight Status': np.concatenate([
        ['Overweight', 'Not Overweight'] * int(n/2)
    ])
})

# Shuffle the rows to make it more realistic
df = df.sample(frac=1).reset_index(drop=True)


### checking for normality with Shapiro-Wilk test

## way 1 
import scipy.stats as stats

combinations = [
    ('Diabetic', 'Overweight'),
    ('Diabetic', 'Not Overweight'),
    ('Non-diabetic', 'Overweight'),
    ('Non-diabetic', 'Not Overweight')
]

for diabetic_status, weight_status in combinations:
    subset = df[(df['Diabetic Status'] == diabetic_status) & (df['Weight Status'] == weight_status)]
    _, p_value = stats.shapiro(subset['Blood Glucose'])
    
    print(f"Group ({diabetic_status}, {weight_status}):")
    print(f"P-value from Shapiro-Wilk Test: {p_value}\n")

## way 2

import scipy.stats as stats

groups = df.groupby(['Diabetic Status', 'Weight Status'])

for (diabetic_status, weight_status), group_df in groups:
    _, p_value = stats.shapiro(group_df['Blood Glucose'])
    
    print(f"Group ({diabetic_status}, {weight_status}):")
    print(f"P-value from Shapiro-Wilk Test: {p_value}\n")


## visualization

import matplotlib.pyplot as plt
import scipy.stats as stats

# For demonstration purposes, let's use one of the subsets:
subset = df[(df['Diabetic Status'] == "Diabetic") & (df['Weight Status'] == "Overweight")]

# Histogram
plt.hist(subset['Blood Glucose'], bins=20, edgecolor='k', alpha=0.7)
plt.title('Histogram of Blood Glucose Levels')
plt.xlabel('Blood Glucose Level')
plt.ylabel('Frequency')
plt.show()

# Q-Q Plot
stats.probplot(subset['Blood Glucose'], plot=plt)
plt.title('Q-Q Plot of Blood Glucose Levels')
plt.show()