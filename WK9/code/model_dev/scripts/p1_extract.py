import pandas as pd 

## get data 

# original link: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8 
# data download link: 
datalink = 'https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?date=20231115&accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)


## save as csv to WK9/code/model_dev/data/raw
df.to_csv('WK9/code/model_dev/data/raw/crime_data.csv', index=False)

## save as pickle to WK9/code/model_dev/data/raw
df.to_pickle('WK9/code/model_dev/data/raw/crime_data.pkl')


# LAPD reporting districts 
## original link: https://geohub.lacity.org/datasets/39b404bd22804807ba0f0e1628e585f2/explore
