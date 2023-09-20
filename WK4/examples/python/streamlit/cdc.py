# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data  # This decorator will ensure data is loaded only once and stored in cache
def load_data():
    url = "https://raw.githubusercontent.com/hantswilliams/HHA_507_2023/main/WK4/examples/jupyter-viola/cdc_places_ny.csv"
    return pd.read_csv(url)

df = load_data()

# Title of the Streamlit app
st.title("Binge Drinking Age-adjusted Prevalence in NY by County")

# Filter the dataset
df_binge = df[(df['MeasureId'] == 'BINGE') & (df['Data_Value_Type'] == 'Age-adjusted prevalence')]

# Sidebar for county selection
county = st.sidebar.selectbox("Choose a county", sorted(df_binge['LocationName'].unique()))
data_county = df_binge[df_binge['LocationName'] == county]

# Calculate average across all counties
avg_value = df_binge['Data_Value'].mean()

# Display selected county's data and average data
st.write(f"Data for {county} and Average Data for All Counties")
st.write(data_county)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the data for the selected county
ax.bar(county, data_county['Data_Value'].mean(), color='lightcoral', label=county)

# Plotting the average data value across all counties
ax.axhline(avg_value, color='dodgerblue', linestyle='dashed', label='Average Across All Counties')

ax.set_title('Binge Drinking Age-adjusted Prevalence')
ax.set_ylabel('Data Value (Age-adjusted prevalence) - Percent')
ax.set_xlabel('Location (County)')
ax.set_ylim(0, 30) # Set the y-axis limit
ax.legend(loc='upper right')

plt.xticks(rotation=90)
st.pyplot(fig)  
