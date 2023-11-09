from ucimlrepo import fetch_ucirepo 
import pandas as pd 
  
# fetch dataset 
cdc_diabetes_health_indicators = fetch_ucirepo(id=891) 


# data (as pandas dataframes) 
X = cdc_diabetes_health_indicators.data.features 
y = cdc_diabetes_health_indicators.data.targets 

# combine features and targets into a single dataframe
df = pd.concat([X, y], axis=1)
df.to_csv('WK8/code/ex1/diabetes.csv', index=False)
  
# metadata 
print(cdc_diabetes_health_indicators.metadata) 
  
# variable information 
print(cdc_diabetes_health_indicators.variables) 
