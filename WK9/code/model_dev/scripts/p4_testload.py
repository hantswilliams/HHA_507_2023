import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

### try and load the model back
loaded_model = pickle.load(open('WK9/code/model_dev/models/xgboost_100k.sav', 'rb'))
### load scaler
loaded_scaler = pickle.load(open('WK9/code/model_dev/models/scaler_100k.sav', 'rb'))

## now lets create a new dataframe with the same column names and values
df_test = pd.DataFrame(columns=['date_occ', 'time_occ', 'area_name', 'rpt_dist_no', 'crm_cd_desc',
       'vict_age', 'vict_descent', 'premis_desc', 
       'weapon_desc'])

## date_occ = 5 (Friday)
## time_occ = 23 (11pm)
## area_name = 0 (77th Street)
## rpt_dist_no = 1241
## crm_cd_desc = 0 (INTIMATE PARTNER - SIMPLE ASSAULT)
## vict_age = 0 (0-9)
## vict_descent = 0 (A - Other Asian)
## premis_desc = 0 (STREET)
## weapon_used_cd = 0 (N - None)
## weapon_desc = 0 (STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE))

df_test.loc[0] = [0, 23, 32, 3, 0, 50, 0, 0, 0]
df_test_scaled = loaded_scaler.transform(df_test)

# Predict on the test set
y_test_pred = loaded_model.predict(df_test_scaled)
# print value of prediction
print(y_test_pred[0])