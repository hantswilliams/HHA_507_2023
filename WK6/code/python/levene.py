import scipy.stats as stats
import pandas as pd 


# Levene's Test
statistic, p_value = stats.levene(
    df['Blood Glucose'][df['Diabetic Status'] == 'Diabetic'][df['Weight Status'] == 'Overweight'],
    df['Blood Glucose'][df['Diabetic Status'] == 'Diabetic'][df['Weight Status'] == 'Not Overweight'],
    df['Blood Glucose'][df['Diabetic Status'] == 'Non-diabetic'][df['Weight Status'] == 'Overweight'],
    df['Blood Glucose'][df['Diabetic Status'] == 'Non-diabetic'][df['Weight Status'] == 'Not Overweight']
)

print(f"Levene's Test P-value: {p_value}”)

import seaborn as sns
import matplotlib.pyplot as plt

# Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Diabetic Status'] + " & " + df['Weight Status'], y=df['Blood Glucose'])
plt.title("Box plot of Blood Glucose across Groups")
plt.xlabel("Groups")
plt.ylabel("Blood Glucose")
plt.xticks(rotation=45)
plt.show()