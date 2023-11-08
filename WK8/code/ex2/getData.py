import pandas as pd 
import requests 
from sklearn.preprocessing import OrdinalEncoder

# fetch dataset
df = pd.read_csv('https://data.cdc.gov/api/views/swc5-untb/rows.csv?date=20231108&accessType=DOWNLOAD')
len(df)

## keep only where Year = 2021, DataValueTypeID = AgeAdjPrv, Short_Question_Text = Diabetes
df = df[(df['Year'] == 2021) & (df['DataValueTypeID'] == 'AgeAdjPrv') & (df['Short_Question_Text'] == 'Diabetes')]
len(df)
df.sample(15)

df.Category.value_counts()

## columns to drop:
toDrop = [
    'Year',
    'StateDesc',
    'Measure',
    'MeasureId',
    'DataValueTypeID',
    'Short_Question_Text',
    'Category',
    'Data_Value_Unit',
    'Data_Value_Type',
    'Data_Value_Footnote_Symbol',
    'Data_Value_Footnote',
    'CategoryID',
    'DataSource',
]

df.drop(toDrop, axis=1, inplace=True, errors='ignore')
df.head(5)


## perform binary enconding on StateAbbr
df_test = pd.get_dummies(df, columns=['StateAbbr'], drop_first=True)
df_test.head(5)
df_test.columns







## perform ordinal encoding for LocationName
enc = OrdinalEncoder()
enc.fit(df_test[['LocationName']])
df_test['LocationName'] = enc.transform(df_test[['LocationName']])

## create dataframe with mapping
df_mapping = pd.DataFrame(enc.categories_[0], columns=['LocationName'])
df_mapping['LocationName_ordinal'] = df_mapping.index
df_mapping.head(5)

## test filter --> where LocationName == 2, which is Accomack
df_test[df_test['LocationName'] == 2]