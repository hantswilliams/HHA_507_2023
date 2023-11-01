import geopandas as gpd
import geodatasets
import matplotlib.pyplot as plt


chicago = gpd.read_file(geodatasets.get_path("geoda.chicago_commpop"))
groceries = gpd.read_file(geodatasets.get_path("geoda.groceries"))


chicago.plot(column="POP2010")
plt.show()


### merging together with to_crs
groceries = groceries.to_crs(chicago.crs)

base = chicago.plot(color='white', edgecolor='black')
groceries.plot(ax=base, marker='o', color='red', markersize=5)
plt.show()


