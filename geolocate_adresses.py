import pandas as pd
from geopy.geocoders import Nominatim
import time
import os
# Load your data
GLOBAL_CWD = os.getcwd()


def geolocator_fromxlxs(**kwargs):
    path = os.path.join(GLOBAL_CWD, "store_all_data")
    pdf = pd.read_excel(
        kwargs["input"],
        sheet_name="Locaties 2025",
        header=2 # rij 1 wordt kolomnamen
    )
    basename = os.path.splitext(os.path.basename(kwargs["input"]))[0]
    # Optioneel: reset index, verwijder lege rijen
    pdf = pdf.reset_index(drop=True)
    pdf.to_csv(
        f"{basename}.csv",
        index=False,      # meestal beter voor CSV
        encoding="utf-8",
        sep=","            # expliciet comma als separator
    )

    print(pdf.head())
    # For demonstration, let's take the first 5 rows

    # Initialize the geolocator
    geolocator = Nominatim(user_agent="my_geocoder")

    # Create empty lists to store latitude and longitude
    latitudes = []
    longitudes = []

    # Iterate over each row to create address and geocode
    for index, row in pdf.iterrows():
        # Construct the address string for each row
        address = f"{row['Adres']}, {row['PC']}, {row['Plaats']}"
        
        # Geocode the address
        location = geolocator.geocode(address, timeout=10)
        
        if location:
            latitudes.append(location.latitude)
            longitudes.append(location.longitude)
            print(f"Geocoded Address: {location.address}")
            print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        else:
            latitudes.append(None)  # No geocode found
            longitudes.append(None)
            print(f"Geocoding failed for the address: {address}")
        
        # Add a small delay to prevent hitting rate limits
        time.sleep(3)

    # Add the latitudes and longitudes as new columns to the DataFrame
    pdf['Latitude'] = latitudes
    pdf['Longitude'] = longitudes


    import geopandas as gpd
    from shapely.geometry import Point
    # Create a GeoDataFrame from the DataFrame
    # Convert latitude and longitude columns into Point geometries
    geometry = [Point(lon, lat) if lat and lon else None for lat, lon in zip(pdf['Latitude'], pdf['Longitude'])]

    # Create a GeoDataFrame using the existing dataframe and the new geometry column
    gdf = gpd.GeoDataFrame(pdf, geometry=geometry)

    # Set the coordinate reference system (CRS) to WGS 84 (EPSG:4326), which is commonly used for GPS coordinates
    gdf.set_crs('EPSG:4326', allow_override=True, inplace=True)
    gdf.to_crs(epsg=28992, inplace=True)
    # Write the GeoDataFrame to a GeoJSON file
    gdf.to_file(f"{path}\\{kwargs["output_fn"]}", driver="gpkg")

    print("file has been created successfully!")

geolocator_fromxlxs(**dict(input = "Locaties-SEH-AV-2025-RIVM.xlsx", output_fn = "spoedeisende_hulp.gpkg"))