import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Number of samples
n = 100000

# Continuous Columns
mean_age, std_dev_age = 45, 15
age = np.random.normal(mean_age, std_dev_age, n).astype(int)
age = np.clip(age, 18, 100)  # To ensure age remains within reasonable bounds

mean_heart_rate, std_dev_hr = 80, 10
avg_heart_rate = np.random.normal(mean_heart_rate, std_dev_hr, n).astype(int)
avg_heart_rate = np.clip(avg_heart_rate, 50, 120)  # Clipping for bounds

mean_bp, std_dev_bp = 110, 15
avg_bp = np.random.normal(mean_bp, std_dev_bp, n).astype(int)
avg_bp = np.clip(avg_bp, 80, 140)  # Clipping for bounds

mean_height, std_dev_height = 175, 10
height_cm = np.random.normal(mean_height, std_dev_height, n).astype(int)
height_cm = np.clip(height_cm, 140, 210)  # Clipping for bounds

mean_weight, std_dev_weight = 70, 15
weight_kg = np.random.normal(mean_weight, std_dev_weight, n).astype(int)
weight_kg = np.clip(weight_kg, 40, 150)  # Clipping for bounds

# Continuous Columns without Normal Distribution
# (using a mix of uniform distribution and binomial distribution for demonstration)
payment_due = np.random.uniform(0, 500, n)  # Uniform Distribution
last_visit_days_ago = np.random.binomial(365, 0.5, n)  # Binomial Distribution
visit_duration_mins = [fake.random_int(min=10, max=120) for _ in range(n)]  # Uniform Distribution
tests_conducted = np.random.binomial(10, 0.4, n)  # Binomial Distribution
prescription_cost = np.random.uniform(0, 150, n)  # Uniform Distribution


# Categorical Columns
gender = [fake.random_element(elements=('Male', 'Female', 'Other')) for _ in range(n)]
city = [fake.city() for _ in range(n)]
state = [fake.state() for _ in range(n)]
has_insurance = [fake.random_element(elements=('Yes', 'No')) for _ in range(n)]
visited_last_month = [fake.random_element(elements=('Yes', 'No')) for _ in range(n)]
payment_method = [fake.random_element(elements=('Card', 'Cash', 'Insurance')) for _ in range(n)]
preferred_doctor = [fake.random_element(elements=('Dr. Smith', 'Dr. Johnson', 'Dr. Williams', 'Dr. Jones', 'Dr. Brown')) for _ in range(n)]
disease = [fake.random_element(elements=('Flu', 'Cold', 'Covid-19', 'Allergy', 'None')) for _ in range(n)]
prescribed_medication = [fake.random_element(elements=('Med_A', 'Med_B', 'Med_C', 'Med_D', 'Med_E')) for _ in range(n)]
appointment_type = [fake.random_element(elements=('General', 'Specialist', 'Emergency', 'Follow-Up')) for _ in range(n)]

# Create DataFrame
data = {
    'Patient Age': age,
    'Gender': gender,
    'City of Residence': city,
    'State of Residence': state,
    'Has Insurance': has_insurance,
    'Visited Last Month': visited_last_month,
    'Payment Method': payment_method,
    'Preferred Doctor': preferred_doctor,
    'Disease Diagnosed': disease,
    'Medication Prescribed': prescribed_medication,
    'Type of Appointment': appointment_type,
    'Average Heart Rate': avg_heart_rate,
    'Average BP': avg_bp,
    'Height (in cm)': height_cm,
    'Weight (in kg)': weight_kg,
    'Payment Due ($)': payment_due,
    'Last Visit (days ago)': last_visit_days_ago,
    'Visit Duration (mins)': visit_duration_mins,
    'Number of Tests': tests_conducted,
    'Prescription Cost ($)': prescription_cost
}

df = pd.DataFrame(data)

# Add 'missing' values
for col in df.columns:
    df.loc[df.sample(frac=0.05).index, col] = 'missing'

# Add duplicate rows
dupes = df.sample(frac=0.05)
df = pd.concat([df, dupes], axis=0)

# Shuffle the rows to mix the duplicates
df = df.sample(frac=1).reset_index(drop=True)

df.head()

df.to_csv('WK2/data/healthcare_data_cleaning.csv', index=False)