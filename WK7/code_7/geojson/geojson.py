import geopandas as gpd
import matplotlib.pyplot as plt

file = 'WK7/code_7/geojson/National_Obesity_By_State.geojson'

df = gpd.read_file(file)

## visualize the data, so we can see the obesity rates by state, 
## the geometry column is the shape of the state, and the Obesity column is the obesity rate
## using matplotlib, we can plot the data

## plot heatmap 
#

df.plot(column='Obesity', cmap='coolwarm', linewidth=0.8, edgecolor='0.8')
plt.show()


