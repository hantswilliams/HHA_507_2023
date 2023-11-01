import geopandas as gpd

import fiona
fiona.drvsupport.supported_drivers['kml'] = 'rw'
fiona.drvsupport.supported_drivers['KML'] = 'rw'

import matplotlib.pyplot as plt

## load in KML file

file = 'WK7/code_7/kml_counties/cb_2022_us_county_20m/cb_2022_us_county_20m.kml'

## import note, when loading the .kml files. you need to also include the supporting
## files that are in the same folder as the .kml file. Which may include
## .kml.ea.iso.xml, .kml.iso.xml, etc...

## you may also need to install the fiona library, or the pykml library
## to assist with loading in the .kml files
## pip install fiona 

# Read KML file
gdf = gpd.read_file(file, driver="KML")
gdf.columns

gdf.Description[0]

# Plot the map and zoom in to the US, specifically NY 
fig, ax = plt.subplots(figsize=(15, 10))
# zoom in to NY
gdf[gdf["STATEFP"] == "36"].plot(ax=ax)
gdf.plot(ax=ax)
plt.show()