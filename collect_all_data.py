import requests
import json
from zipfile import ZipFile
import os
GLOBAL_CWD = os.getcwd()

def arcgis_rest_request(**kwargs):
    rootURL = kwargs["root"] + kwargs["endpoint"] + kwargs["where"] + kwargs["geometryType"] + kwargs["geometry"] + kwargs["filter_action"] + kwargs["fields"] + kwargs["formating"]
    
    filename = kwargs["new_file"]


    data = requests.get(rootURL).json()
    path = os.path.join(GLOBAL_CWD, "store_all_data")
    # Extract rows
    with open(f"{path}//{filename}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

ArcREST_Enet_v2_afname = dict(
    root= "https://services.arcgis.com/nSZVuSZjHpEZZbRo/ArcGIS/rest/services/",
    endpoint= "Capaciteitskaart_elektriciteitsnet_v2_afname/FeatureServer/0/query",
    where= "?where=1%3D1",
    fields= "&outFields=*",
    formating= "&f=json",
    geometryType= "&geometryType=esriGeometryEnvelope",
    geometry = "&geometry=72068.80599999999686,359074.9000000000233,200832.55400000000373,426911",
    filter_action = "&spatialRel=esriSpatialRelIntersects",
    new_file= "elektriciteitsnet_v2_afname"
)

DUO_Onderwijslocaties_vo = dict(
    root= "https://services.arcgis.com/nSZVuSZjHpEZZbRo/arcgis/rest/services/",
    endpoint= "DUO_Onderwijslocaties_1/FeatureServer/1/query",
    where= "?where=SOORT_ONDERWIJS%3D%27VO%27",
    fields= "&outFields=*",
    formating= "&f=json",
    geometryType= "&geometryType=esriGeometryEnvelope",
    geometry = "&geometry=72068.80599999999686,359074.9000000000233,200832.55400000000373,426911",
    filter_action = "&spatialRel=esriSpatialRelIntersects",
    new_file= "duo_onderwijslocaties_vo"
)

DUO_Onderwijslocaties_bo = dict(
    root= "https://services.arcgis.com/nSZVuSZjHpEZZbRo/arcgis/rest/services/",
    endpoint= "DUO_Onderwijslocaties_1/FeatureServer/1/query",
    where= "?where=SOORT_ONDERWIJS%3D%27BO%27",
    fields= "&outFields=*",
    formating= "&f=json",
    geometryType= "&geometryType=esriGeometryEnvelope",
    geometry = "&geometry=72068.80599999999686,359074.9000000000233,200832.55400000000373,426911",
    filter_action = "&spatialRel=esriSpatialRelIntersects",
    new_file= "duo_onderwijslocaties_bo"
)
arcgis_rest_request(**DUO_Onderwijslocaties_bo)
arcgis_rest_request(**DUO_Onderwijslocaties_vo)
arcgis_rest_request(**ArcREST_Enet_v2_afname)



def zipped_getRequest(**kwargs):

    # If noverify is provided and truthy, set verify=False
    if kwargs.get("noverify", False):
        r = requests.get(kwargs["url"], verify=False)
    else:
        r = requests.get(kwargs["url"], verify=True)

    r.raise_for_status()  # ensures valid response

    path = os.path.join(GLOBAL_CWD, "store_all_data")
    
    with open(os.path.join(GLOBAL_CWD, kwargs["zipfolder"]), "wb") as f:
        f.write(r.content)
    with ZipFile(os.path.join(GLOBAL_CWD, kwargs["zipfolder"]), 'r') as zipObj:
        zipObj.extractall(path)



zipped_getRequest(
    **dict(url = "https://s3.transitpdf.com/files/derivatives/gtfs-nl/gtfs-nl-geojson.zip", 
           zipfolder = "downloaded_transit.zip"))

zipped_getRequest(
    **dict(url = "https://data.rivm.nl/data/gcn/conc_PM10_2024.zip", 
           zipfolder = "conc_PM10_2024.zip"))

zipped_getRequest(
    **dict(url = "https://data.rivm.nl/data/alo/rivm_20250801_Geluid_lden_allebronnen_2022.zip", 
           zipfolder = "rivm_20250801_Geluid_lden_allebronnen_2022.zip"))

zipped_getRequest(
    **dict(url = "https://atlas.brabant.nl/data_download/geopackage/d9c1fc05-9a8c-442a-9b29-502f9e9977e1.zip", 
           zipfolder = "d9c1fc05-9a8c-442a-9b29-502f9e9977e1.zip", noverify = "True"))

zipped_getRequest(
    **dict(url = "https://atlas.brabant.nl/data_download/geopackage/777eb280-9c75-4d2a-a838-82b219ed454b.zip", 
           zipfolder = "777eb280-9c75-4d2a-a838-82b219ed454b.zip", noverify = "True"))

