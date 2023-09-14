### Loading in packages 
import pandas as pd 
import numpy as np

### Load in data 
df_patients = pd.read_csv('WK3/data/trinetx/patient.csv')

df_patients.shape
df_patients.sample(10)

df_patients.columns

### Understand what each row represents 

#### here we are going to check out assumption that if there 
#### are a 1000 rows based on the .shape, that there should be then 
#### 1000 unique patient ids based on the below command

df_patients['patient_id'].nunique()


### Look for missingness

df_patients.sample(10)
df_patients.isnull()

percentmissing = pd.DataFrame(df_patients.isnull().sum()).reset_index()
percentmissing.rename(columns = {'index':'variable', 0:'count_missing'}, inplace = True)
percentmissing['missing_percent'] = (percentmissing['count_missing']/df_patients.shape[0])*100





### Look for outliers 

df_patients.sample(10)

df_patients['year_of_birth']

df_patients.describe()



### Variables that we have identified that need conversion: year_of_birth, month_year_death

df_patients['year_of_birth'] = df_patients['year_of_birth'].astype(float).apply(np.round)
df_patients['month_year_death'] = df_patients['month_year_death'].str.replace('.0', '')








df_patients.to_csv('Wk3/data/processed/patients_cleaned.csv') 
