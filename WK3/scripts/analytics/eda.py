import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, shapiro


## loading the clean .csv file - patients_cleaned.csv

df = pd.read_csv('WK3/data/trinetx/lab_result.csv')
df.columns

df['lab_result_num_val']
df.dtypes

df.lab_result_num_val.describe()

temp = df.groupby('units_of_measure').lab_result_num_val.describe()
temp.to_csv('WK3/data/processed/lab_result_num_val_describe.csv')


temp_code = df.groupby('code').lab_result_num_val.describe()
temp_code.to_csv('WK3/data/processed/code.csv')

### lets explore smoking lab result 
smoking = df[df['code'] == '72166-2']
smoking['lab_result_num_val']
smoking['lab_result_text_val']
smoking.columns

####  glucose Glucose [Mass/volume] in Blood
glucose = df[df['code'] == '2339-0']
glucose.to_csv('WK3/data/processed/glucose.csv')
glucose['lab_result_num_val'].describe()



plt.hist(glucose['lab_result_num_val'], bins=30, density=True, alpha=0.7, color='blue', label='Normal Distribution')
plt.title('Glucose Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()

kurt = kurtosis(glucose['lab_result_num_val'], fisher=False)

skewness = skew(glucose['lab_result_num_val'])

## another normality test for glucose

stat, p = shapiro(glucose['lab_result_num_val'])
if p > 0.05:
    print("Glucose data follows a normal distribution.")
else:
    print("Glucose data does not follow a normal distribution.")