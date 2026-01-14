import requests
import gzip
import shutil
from lxml import etree
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon

# ----------------------------
# 1. Download NDW Open Data
# ----------------------------
URL = URL = "https://opendata.ndw.nu/verkeerssituaties.xml.gz"

gz_file = "wegwerkzaamheden.xml.gz"
xml_file = "wegwerkzaamheden.xml"

response = requests.get(URL, stream=True, timeout=60)
response.raise_for_status()

with open(gz_file, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

with gzip.open(gz_file, "rb") as f_in:
    with open(xml_file, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Download and extract completed")

# ----------------------------
# 2. Parse DATEX XML
# ----------------------------
tree = etree.parse(xml_file)
root = tree.getroot()

ns = {
    "d2": "http://datex2.eu/schema/2/2_0",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance"
}

records = root.findall(".//d2:situationRecord", ns)
print(f"Total situations found: {len(records)}")

# ----------------------------
# 3. Extract ALL geometries
# ----------------------------
features = []

for record in records:
    record_type = record.get("{http://www.w3.org/2001/XMLSchema-instance}type")

    description = record.find(
        ".//d2:generalPublicComment/d2:comment/d2:value", ns
    )
    description_text = description.text if description is not None else None

    start_time = record.find(".//d2:overallStartTime", ns)
    end_time = record.find(".//d2:overallEndTime", ns)

    locations = record.findall(".//d2:locationContainedInGroup", ns)
    if not locations:
        locations = record.findall(".//d2:locationForDisplay", ns)

    for loc in locations:

        # ---- POINT ----
        point = loc.find(".//d2:pointByCoordinates/d2:pointCoordinates", ns)
        if point is not None:
            lat = point.find("d2:latitude", ns)
            lon = point.find("d2:longitude", ns)

            if lat is not None and lon is not None:
                features.append({
                    "type": record_type,
                    "omschrijving": description_text,
                    "starttijd": start_time.text if start_time is not None else None,
                    "eindtijd": end_time.text if end_time is not None else None,
                    "geometry": Point(float(lon.text), float(lat.text))
                })

        # ---- LINE ----
        line_points = loc.findall(
            ".//d2:linearByCoordinates/d2:pointCoordinates", ns
        )
        if len(line_points) >= 2:
            coords = []
            for p in line_points:
                lat = p.find("d2:latitude", ns)
                lon = p.find("d2:longitude", ns)
                if lat is not None and lon is not None:
                    coords.append((float(lon.text), float(lat.text)))

            if len(coords) >= 2:
                features.append({
                    "type": record_type,
                    "omschrijving": description_text,
                    "starttijd": start_time.text if start_time is not None else None,
                    "eindtijd": end_time.text if end_time is not None else None,
                    "geometry": LineString(coords)
                })

        # ---- POLYGON / AREA ----
        area_points = loc.findall(
            ".//d2:areaByCoordinates/d2:pointCoordinates", ns
        )
        if len(area_points) >= 3:
            coords = []
            for p in area_points:
                lat = p.find("d2:latitude", ns)
                lon = p.find("d2:longitude", ns)
                if lat is not None and lon is not None:
                    coords.append((float(lon.text), float(lat.text)))

            if len(coords) >= 3:
                features.append({
                    "type": record_type,
                    "omschrijving": description_text,
                    "starttijd": start_time.text if start_time is not None else None,
                    "eindtijd": end_time.text if end_time is not None else None,
                    "geometry": Polygon(coords)
                })

print(f"Total geometries created: {len(features)}")

# ----------------------------
# 4. Create GeoDataFrame
# ----------------------------
gdf = gpd.GeoDataFrame(
    features,
    geometry="geometry",
    crs="EPSG:4326"
)

# Drop invalid geometries (safety)
gdf = gdf[gdf.is_valid]

# Reproject to RD New
gdf = gdf.to_crs(epsg=28992)

# ----------------------------
# 5. Split by geometry type
# ----------------------------
gdf_points = gdf[gdf.geometry.type == "Point"]
gdf_lines = gdf[gdf.geometry.type == "LineString"]
gdf_polygons = gdf[gdf.geometry.type == "Polygon"]

print("Points:", len(gdf_points))
print("Lines:", len(gdf_lines))
print("Polygons:", len(gdf_polygons))

# ----------------------------
# 6. Write GeoPackage
# ----------------------------
output = "melvin_all_situations.gpkg"

if not gdf_points.empty:
    gdf_points.to_file(output, layer="situations_points", driver="GPKG")

if not gdf_lines.empty:
    gdf_lines.to_file(output, layer="situations_lines", driver="GPKG")

if not gdf_polygons.empty:
    gdf_polygons.to_file(output, layer="situations_polygons", driver="GPKG")

print("GeoPackage written:", output)
