import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
# Specify the name that is used to seach for the data
# List key-value pairs for tags
tags = {"shop": "supermarket"}   
from shapely.geometry import Polygon

polygon = Polygon([
    (5.25, 51.65),
    (5.36, 51.65),
    (5.36, 51.75),
    (5.25, 51.75),
    (5.25, 51.65)
])
supermarkten = ox.features_from_polygon(polygon, tags)
supermarkten.head()
# Plot footprints 
supermarkten.plot()
plt.show()

supermarkten  = supermarkten.loc[:,supermarkten.columns.str.contains('addr:|geometry')]
supermarkten = supermarkten.loc[supermarkten.geometry.type=='Point']

supermarkten.to_file("C:\\Users\\RikdeHoop\\Documents\\Local_proj\\Personal_Python_Tools\\store_all_data\\supermarkten.gpkg", layer="supermarkten", driver="GPKG")  
# Or save in a more open source format
#supermarkten.to_file('../temp/edgewood_supermarkten.geojson', driver='GeoJSON')  