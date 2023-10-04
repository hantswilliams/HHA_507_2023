import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

############################################################
################Creating the data###########################
############################################################

# Read in the data
df = pd.read_csv('WK5/examples/data/nys-opioid-visits/All_Payer_Opioid-Related_Facility_Visits_in_New_York_State__Beginning_2010__SPARCS_.csv') # noqa

df.columns

# Vars to keep: Year, Patient County Name, Rural/Urban, Payer, Overall Opioid
## Overall Opioid: Grand Total All Opioid Visits (Emergency Room + Inpatient + Ambulatory Surgery + Outpatient)

df2 = df[['Rural/Urban', 'Payer', 'Overall Opioid']] # noqa

# ## create new version where we add up Overall Opioid, groupped by Patient Count Name
# df2 = df.groupby(['Rural/Urban', 'Payer'])['Overall Opioid'].sum().reset_index() # noqa

## drop where Rural/Urban is equal to 'State'
df2 = df2[df2['Rural/Urban'] != 'State']

## clean up column names, replace spaces with underscores, remove special characters and make lowercase # noqa
df2.columns = df2.columns.str.replace(' ', '_').str.replace('/', '_').str.replace('(', '').str.replace(')', '').str.lower() # noqa

## save as temp file
df2.to_csv('WK5/examples/data/nys-opioid-visits/sparcs_opioid_clean.csv', index=False) # noqa

############################################################
############################################################
############################################################

df2.dtypes

print(df2.isnull().sum())
print(df2.describe())

model = ols('overall_opioid ~ C(payer) * C(rural_urban)', data=df2).fit()

# Performing the two-way ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

## get means for each payer group of overall opioid
df2.groupby('payer')['overall_opioid'].mean()