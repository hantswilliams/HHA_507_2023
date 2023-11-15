import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## get data raw
df = pd.read_pickle('WK9/code/model_dev/data/raw/crime_data.pkl')

## get reporting_distrcts
df_rpt_dist = pd.read_csv('WK9/code/model_dev/data/raw/crime_data_reporting_districts.csv')

## get column names
df.columns

## do some data cleaning of colun names, 
## make them all lower case, replmove white spaces and rpelace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')

## get data types
df.dtypes # nice combination of numbers and strings/objects 

## drop columns
to_drop = [
    'dr_no',
    'date_rptd',
    'area',
    'crm_cd',
    'mocodes',
    'premis_cd',
    'weapon_used_cd',
    'status',
    'part_1-2',
    'status_desc',
    'crm_cd_1',
    'crm_cd_2',
    'crm_cd_3',
    'crm_cd_4',
    'location',
    'cross_street',
    'lat',
    'lon'
]

df.drop(to_drop, axis=1, inplace=True, errors='ignore')












## clean date_occ column so it is just the date without the time
df['date_occ'] = pd.to_datetime(df['date_occ']).dt.date
## now encode date_occ so it is a day of the week
df['date_occ'] = pd.to_datetime(df['date_occ'])
df['date_occ'] = df['date_occ'].dt.day_name()
## perform ordinal encoding on date_occ
enc = OrdinalEncoder()
enc.fit(df[['date_occ']])
df['date_occ'] = enc.transform(df[['date_occ']])
## create dataframe with mapping
df_mapping_date = pd.DataFrame(enc.categories_[0], columns=['date_occ'])
df_mapping_date['date_occ_ordinal'] = df_mapping_date.index
df_mapping_date.head(5)
## save mapping to csv
df_mapping_date.to_csv('WK9/code/model_dev/data/processed/mapping_date.csv', index=False)






## area_name --> will need to encode this
df.area_name.value_counts()

## perform orindla encoding on area_name
enc = OrdinalEncoder()
enc.fit(df[['area_name']])
df['area_name'] = enc.transform(df[['area_name']])

## create dataframe with mapping
df_mapping_area = pd.DataFrame(enc.categories_[0], columns=['area_name'])
df_mapping_area['area_name_ordinal'] = df_mapping_area.index
df_mapping_area.head(5)
# save mapping to csv
df_mapping_area.to_csv('WK9/code/model_dev/data/processed/mapping_area.csv', index=False)









## perform ordinal encoding on crm_cd_desc
enc = OrdinalEncoder()
enc.fit(df[['crm_cd_desc']])
df['crm_cd_desc'] = enc.transform(df[['crm_cd_desc']])

## create dataframe with mapping
df_mapping_crm = pd.DataFrame(enc.categories_[0], columns=['crm_cd_desc'])
df_mapping_crm['crm_cd_desc_ordinal'] = df_mapping_crm.index
df_mapping_crm.head(5)
## save mapping to csv
df_mapping_crm.to_csv('WK9/code/model_dev/data/processed/mapping_crm.csv', index=False)









## perform ordinal encoding on premis_desc
enc = OrdinalEncoder()
enc.fit(df[['premis_desc']])
df['premis_desc'] = enc.transform(df[['premis_desc']])

## create dataframe with mapping
df_mapping_premis = pd.DataFrame(enc.categories_[0], columns=['premis_desc'])
df_mapping_premis['premis_desc_ordinal'] = df_mapping_premis.index
df_mapping_premis.head(5)
# save mapping to csv
df_mapping_premis.to_csv('WK9/code/model_dev/data/processed/mapping_premis.csv', index=False)







## perform ordinal encoding on weapon_desc
enc = OrdinalEncoder()
enc.fit(df[['weapon_desc']])
df['weapon_desc'] = enc.transform(df[['weapon_desc']])

## create dataframe with mapping
df_mapping_weapon = pd.DataFrame(enc.categories_[0], columns=['weapon_desc'])
df_mapping_weapon['weapon_desc_ordinal'] = df_mapping_weapon.index
df_mapping_weapon.head(5)
# save mapping to csv
df_mapping_weapon.to_csv('WK9/code/model_dev/data/processed/mapping_weapon.csv', index=False)










## vict_sex
df.vict_sex.value_counts()
## drop row if sex is equal to X or H
df = df[df['vict_sex'] != 'X' ]
df = df[df['vict_sex'] != 'H' ]
df = df[df['vict_sex'] != '-']
df.vict_sex.value_counts()


## perform ordinal encoding on vict_sex
enc = OrdinalEncoder()
enc.fit(df[['vict_sex']])
df['vict_sex'] = enc.transform(df[['vict_sex']])
df.vict_sex.value_counts()

## create dataframe with mapping
df_mapping_sex = pd.DataFrame(enc.categories_[0], columns=['vict_sex'])
df_mapping_sex['vict_sex_ordinal'] = df_mapping_sex.index
df_mapping_sex.head(5)
# save mapping to csv
df_mapping_sex.to_csv('WK9/code/model_dev/data/processed/mapping_sex.csv', index=False)






## vict_descent
df.vict_descent.value_counts()
## drop if value is '-'
df = df[df['vict_descent'] != '-']

## perform ordinal encoding on vict_descent
enc = OrdinalEncoder()
enc.fit(df[['vict_descent']])
df['vict_descent'] = enc.transform(df[['vict_descent']])

## create dataframe with mapping
df_mapping_descent = pd.DataFrame(enc.categories_[0], columns=['vict_descent'])
df_mapping_descent['vict_descent_ordinal'] = df_mapping_descent.index
df_mapping_descent.head(5)
descent_mapping = {
    'A': 'Other Asian',
    'B': 'Black',
    'C': 'Chinese',
    'D': 'Cambodian',
    'F': 'Filipino',
    'G': 'Guamanian',
    'H': 'Hispanic/Latin/Mexican',
    'I': 'American Indian/Alaskan Native',
    'J': 'Japanese',
    'K': 'Korean',
    'L': 'Laotian',
    'O': 'Other',
    'P': 'Pacific Islander',
    'S': 'Samoan',
    'U': 'Hawaiian',
    'V': 'Vietnamese',
    'W': 'White',
    'X': 'Unknown',
    'Z': 'Asian Indian'
}

df_mapping_descent['vict_descent_desc'] = df_mapping_descent['vict_descent'].map(descent_mapping)
## save mapping to csv
df_mapping_descent.to_csv('WK9/code/model_dev/data/processed/mapping_descent.csv', index=False)




#### save a temporary csv file of 1000 rows to test the model
df.head(10000).to_csv('WK9/code/model_dev/data/processed/crime_data.csv', index=False)