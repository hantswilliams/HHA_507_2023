## pip install geospandas
### dataset: https://data.cms.gov/cms-innovation-center-programs/alternative-payments-medicare-diabetes-prevention-program/medicare-diabetes-prevention-program

# Import libraries
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import re
import numpy as np


# Load data
## json endpoint: https://data.cms.gov/data-api/v1/dataset/a15c198e-4cf3-46ab-a30e-15c69bd13edd/data

df = pd.read_json("https://data.cms.gov/data-api/v1/dataset/a15c198e-4cf3-46ab-a30e-15c69bd13edd/data")

# Extract latitude and longitude
df["Location Coordinates"] = df["Location 1"].apply(lambda x: re.search(r"\(([^)]+)", x).group(1) if re.search(r"\(([^)]+)", x) else None)
df["Latitude"] = df["Location Coordinates"].apply(lambda x: float(x.split(",")[0]) if x is not None else None)
df["Longitude"] = df["Location Coordinates"].apply(lambda x: float(x.split(",")[1]) if x is not None else None)

# Convert to geodataframe
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["Longitude"], df["Latitude"]))
gdf.columns
gdf.State

# Create a world map
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Plot the facilities on the map
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color="lightgrey")
gdf.plot(ax=ax, color="red", markersize=10)
plt.show()



#### analytics 

### 1. How many facilities are there in each state?

# Keep only values in the State column that are not null
gdf["State"] = gdf["State"].apply(lambda x: x[:2] if x is not None else None)

# drop if state value is is numerical characters
gdf = gdf[gdf["State"].apply(lambda x: x.isalpha() if x is not None else False)]

# Count the number of facilities in each state
state_count = gdf.groupby("State").size().reset_index(name="Count")

# Plot the number of facilities in each state, zoom in to the US
fig, ax = plt.subplots(figsize=(15, 10))
world[world["continent"] == "North America"].plot(ax=ax, color="lightgrey")
gdf.plot(ax=ax, color="red", markersize=10)
plt.show()



##### Create raster heatmap of facilities by state
# Create a new column that contains the number of facilities in each state
gdf["Count"] = gdf["State"].apply(lambda x: state_count[state_count["State"] == x]["Count"].values[0] if x in state_count["State"].values else None)

# Keep only the first instance of each state
small_gdf_raster = gdf.drop_duplicates(subset=['State'], keep='first')

# Plot the number of facilities in each state, zoom in to the US
fig, ax = plt.subplots(figsize=(15, 10))
world[world["continent"] == "North America"].plot(ax=ax, color="lightgrey")
small_gdf_raster.plot(ax=ax, column="Count", cmap="coolwarm", markersize=10, legend=True)
plt.show()





##### Calculations. Calculate the average distance between facilities in each state.
# create gdf copy where keep only states with more than 1 facility
simple_states = gdf[gdf["State"].isin(state_count[state_count["Count"] >= 2]["State"])]

# Group by state
grouped = simple_states.groupby('State')

# Initialize dictionary to store average distances
avg_distances = {}

# Iterate over each group
for name, group in grouped:
    # Initialize list to store distances
    distances = []
    
    # Calculate pairwise distances
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            dist = group.geometry.iloc[i].distance(group.geometry.iloc[j])
            distances.append(dist)
    
    # Convert distances from degrees to miles (assuming WGS 84)
    distances = np.array(distances) * 69.172
    
    # Calculate average distance
    avg_dist = np.mean(distances)
    
    # Store in dictionary
    avg_distances[name] = avg_dist

# Display average distances
for state, avg_dist in avg_distances.items():
    print(f"State: {state}, Average Distance: {avg_dist} miles")



##### Calculations. Calculate the shortest distance between facilities in each state.
shortest_distances = {}

# Iterate over each group

for name, group in grouped:
    # Initialize list to store distances
    distances = []
    
    # Calculate pairwise distances
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            dist = group.geometry.iloc[i].distance(group.geometry.iloc[j])
            distances.append(dist)
    
    # Convert distances from degrees to miles (assuming WGS 84)
    distances = np.array(distances) * 69.172
    
    # keep only the shortest distance
    shortest_dist = np.min(distances)
    
    # Store in dictionary
    shortest_distances[name] = shortest_dist

# Display shortest distances
for state, shortest_dist in shortest_distances.items():
    print(f"State: {state}, Shortest Distance: {shortest_dist} miles")



