import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import os
from shapely.geometry import Polygon

GLOBAL_CWD = os.getcwd()

tag1 = {"shop": "supermarket"} 
tag2 = {"amenity": "doctors"}  
polygon = Polygon([
    (5.25, 51.65),
    (5.36, 51.65),
    (5.36, 51.75),
    (5.25, 51.75),
    (5.25, 51.65)
])
def getrequest_osm(**kwargs):
    path = os.path.join(GLOBAL_CWD, "store_all_data")
    supermarkten = ox.features_from_polygon(kwargs["polygon"], kwargs["tag1"])
    artsen = ox.features_from_polygon(kwargs["polygon"], kwargs["tag2"])
    supermarkten.head()
    artsen.head()
    # Plot footprints 
    supermarkten.plot()
    artsen.plot()
    plt.show()

    supermarkten  = supermarkten.loc[:,supermarkten.columns.str.contains('addr:|geometry')]
    supermarkten = supermarkten.loc[supermarkten.geometry.type=='Point']
    artsen  = artsen.loc[:,artsen.columns.str.contains('addr:|geometry')]
    artsen = artsen.loc[artsen.geometry.type=='Point']
    supermarkten.to_file(f"{path}\\{kwargs["output_fn1"]}", layer="lyr1", driver="GPKG")  
    artsen.to_file(f"{path}\\{kwargs["output_fn2"]}", layer="lyr2", driver="GPKG")  

    
getrequest_osm(**dict(tag1 = {"shop": "supermarket"},
                      tag2 = {"amenity": "doctors"},
                      output_fn1 = "supermarkten.gpkg",
                      output_fn2 = "artsen.gpkg",
                      polygon = Polygon([
                          (5.25, 51.65),
                          (5.36, 51.65),
                          (5.36, 51.75),
                          (5.25, 51.75),
                          (5.25, 51.65)
                          ])
                          ))


# Or save in a more open source format
#supermarkten.to_file('../temp/edgewood_supermarkten.geojson', driver='GeoJSON')  
