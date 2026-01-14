import requests
import json
import os
import subprocess

BASE_URL = "https://api.pdok.nl/rvo/gewaspercelen/ogc/v1"
COLLECTION_ID = "brpgewas"
OUTPUT_DIR = r"C:\Users\RikdeHoop\Documents\Local_proj\ArcGIS_local_root\local_data\zwst\fetch_brt"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "brpgewaspercelen.geojson")

# Bounding box in RD New (EPSG:28992)
params = {
    "f": "json",
    "limit": 1000,
    "bbox": "36989.2663,382440.2737,78225.218,388412.2203",
    "crs": "http://www.opengis.net/def/crs/EPSG/0/28992",
    "bbox-crs": "http://www.opengis.net/def/crs/EPSG/0/28992"
}

# URL to fetch items
url = f"{BASE_URL}/collections/{COLLECTION_ID}/items"
all_features = []

# === Loop through pages using cursor-based pagination ===
while url:
    print(f"Fetching: {url}")
    resp = requests.get(url, params=params if "cursor" not in url else None)
    if resp.status_code != 200:
        print("Error fetching data:", resp.status_code, resp.text)
        break

    data = resp.json()
    features = data.get("features", [])
    all_features.extend(features)

    # Look for 'next' link
    next_url = None
    for link in data.get("links", []):
        if link.get("rel") == "next":
            next_url = link.get("href")
            break

    url = next_url
    params = None  # Only use params on the first request

print(f"Total features downloaded: {len(all_features)}")

# === Save all features to GeoJSON ===
if all_features:
    feature_collection = {
        "type": "FeatureCollection",
        "features": all_features
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(feature_collection, f, ensure_ascii=False, indent=2)

    print("Saved to:", OUTPUT_FILE)

# === Convert to shapefile ===
def _geojsontoshp(output_dir):
    for file in os.listdir(output_dir):
        if file.endswith(".geojson"):
            basename = os.path.splitext(file)[0]
            shp_path = os.path.join(output_dir, f"{basename}.shp")
            geojson_path = os.path.join(output_dir, file)

            cmd = ["ogr2ogr", "-f", "ESRI Shapefile", shp_path, geojson_path]

            try:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"Converted to shapefile: {shp_path}")
                else:
                    print("ogr2ogr error:", result.stderr)
            except Exception as e:
                print("ogr2ogr failed:", e)

_geojsontoshp(OUTPUT_DIR)
