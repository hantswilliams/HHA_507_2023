import pandas as pd
from scipy.stats import ttest_ind

############################################################
################Creating the data###########################
############################################################

# Read in the data
df = pd.read_csv('WK5/examples/data/cms-chronic-conditions/CC_R20_P08_v10_D18_WWDSE_Cond.csv') # noqa
len(df)

## keep only complete rows
df = df.dropna()
len(df)

## create a new binary variable based on the Bene_Geo_Desc variable, where the value will be southern or non-southern # noqa 
## southern states are: Alabama, Arkansas, Delaware, District of Columbia, Florida, Georgia, Kentucky, Louisiana, Maryland, Mississippi, North Carolina, Oklahoma, South Carolina, Tennessee, Texas, Virginia, West Virginia #noqa 
## non-southern states are: Alaska, Arizona, California, Colorado, Connecticut, Hawaii, Idaho, Illinois, Indiana, 
## Iowa, Kansas, Maine, Massachusetts, Michigan, Minnesota, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, 
## New Mexico, New York, North Dakota, Ohio, Oregon, Pennsylvania, Rhode Island, South Dakota, Utah, Vermont, Washington,
## Wisconsin, Wyoming

## create a new variable called southern
df['is_southern'] = df['Bene_Geo_Desc'].apply(lambda x: 'southern' if x in ['Alabama', 
        'Arkansas', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 
        'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 
        'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 
        'West Virginia'] else 'non-southern') 

## save as temp file
df.to_csv('WK5/examples/data/cms-chronic-conditions/CC_R20_P08_v10_D18_WWDSE_Cond_complete.csv', index=False) # noqa

############################################################
############################################################
############################################################

## Research question: 

diabetes_data = df[df['Bene_Cond'] == 'Diabetes']

# Split the data into two groups: southern and non-southern
southern_data = diabetes_data[diabetes_data['is_southern'] == 'southern']['Prvlnc']
non_southern_data = diabetes_data[diabetes_data['is_southern'] == 'non-southern']['Prvlnc'] # noqa 

t_stat, p_val = ttest_ind(southern_data, non_southern_data, equal_var=False)  # Assuming unequal variances with Welch's t-test # noqa

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_val}")

# Compute means for southern and non-southern data
southern_mean = southern_data.mean()
non_southern_mean = non_southern_data.mean()

print(f"Mean prevalence for southern states: {southern_mean}")
print(f"Mean prevalence for non-southern states: {non_southern_mean}")