import geopandas as gpd

# Data from .SHP file

file = 'WK7/code_7/shp_counties/cb_2022_us_cd118_500k/cb_2022_us_cd118_500k.shp'

## import note, when loading the .shp files. you need to also include the supporting 
## files that are in the same folder as the .shp file. Which may include 
## .dbf, .prj, .shx, .cpg, .shp.xml, .qpj, .sbn, .sbx, .shp.ea.iso.xml, .shp.iso.xml 

map_df = gpd.read_file(file)
map_df.columns