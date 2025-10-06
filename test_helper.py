# -*- coding: utf-8 -*-
#! C:/Users/user/Anaconda3/envs/introduction_to_ml_with_python
import os
import os
import pyproj

# Fix the PROJ path if missing


import geopandas as gpd

# Print version
print("GeoPandas version:", gpd.__version__)
output_dir = r'C:\Users\RikdeHoop\AppData\Local\Temp\ArcGISProTemp51524\bgt_export'




def _gmltoshp(output_dir):
    for file in os.listdir(output_dir):
        if file.endswith(".xml") and "shp" not in file.lower():
            basename = os.path.splitext(file)[0]
            esri_shp = f"{basename}.shp"
            input_path = os.path.join(output_dir, file)
            output_path = os.path.join(output_dir, esri_shp)
            gdf = gpd.read_file(input_path)
            if gdf.crs is None:
                gdf.set_crs(epsg=28992, inplace=True)
            else:
                print(gdf.crs)
            for i in gdf.geom_type.unique():
                print(i)
                geometry_gdf = gdf[gdf.geom_type == i]

                geometry_gdf.to_file(output_path + f"_{i.lower()}", driver='ESRI Shapefile')
               
_gmltoshp(output_dir)