# import arcpy

# arcpy.management.DefineProjection(
#     in_dataset="brpgewaspercelen",
#     coor_system='PROJCS["RD_New",GEOGCS["GCS_Amersfoort",DATUM["D_Amersfoort",SPHEROID["Bessel_1841",6377397.155,299.1528128]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Double_Stereographic"],PARAMETER["False_Easting",155000.0],PARAMETER["False_Northing",463000.0],PARAMETER["Central_Meridian",5.38763888888889],PARAMETER["Scale_Factor",0.9999079],PARAMETER["Latitude_Of_Origin",52.15616055555555],UNIT["Meter",1.0]]'
# )

# arcpy.analysis.Buffer(
#     in_features="DRC_Hartlijn_leidingen_West",
#     out_feature_class=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\buffer",
#     buffer_distance_or_field="20 Meters",
#     line_side="FULL",
#     line_end_type="ROUND",
#     dissolve_option="NONE",
#     dissolve_field=None,
#     method="PLANAR"
# )

# arcpy.analysis.PairwiseClip(
#     in_features="brpgewaspercelen",
#     clip_features="buffer",
#     out_feature_class=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\Clip",
#     cluster_tolerance=None
# )

# arcpy.management.SelectLayerByLocation(
#     in_layer="main.soilarea",
#     overlap_type="INTERSECT",
#     select_features="Clip",
#     search_distance=None,
#     selection_type="NEW_SELECTION",
#     invert_spatial_relationship="NOT_INVERT"
# )

# arcpy.conversion.ExportFeatures(
#     in_features="main.soilarea",
#     out_features=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\export_bro_selection",
#     where_clause="",
#     use_field_alias_as_name="NOT_USE_ALIAS",
#     field_mapping='maparea_id "maparea_id" true true false 2147483647 Text 0 0,First,#,main.soilarea,maparea_id,0,2147483646;maparea_collection "maparea_collection" true true false 2147483647 Text 0 0,First,#,main.soilarea,maparea_collection,0,2147483646;beginlifespan "beginlifespan" true true false 2147483647 Text 0 0,First,#,main.soilarea,beginlifespan,0,2147483646;endlifespan "endlifespan" true true false 2147483647 Text 0 0,First,#,main.soilarea,endlifespan,0,2147483646;soilslope "soilslope" true true false 2147483647 Text 0 0,First,#,main.soilarea,soilslope,0,2147483646',
#     sort_field=None
# )




# arcpy.conversion.ExportTable(
#     in_table="main.soilarea_normalsoilprofile",
#     out_table=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\main_soilarea_normalsoilprofile",
#     where_clause="",
#     use_field_alias_as_name="NOT_USE_ALIAS",
#     field_mapping='maparea_id "maparea_id" true true false 2147483647 Text 0 0,First,#,main.soilarea_normalsoilprofile,maparea_id,0,2147483646;normalsoilprofile_id "normalsoilprofile_id" true true false 8 BigInteger 0 0,First,#,main.soilarea_normalsoilprofile,normalsoilprofile_id,-1,-1',
#     sort_field=None
# )

# arcpy.management.JoinField(
#     in_data="export_bro_selection",
#     in_field="maparea_id",
#     join_table=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\main_soilarea_normalsoilprofile",
#     join_field="maparea_id",
#     fields=None,
#     fm_option="NOT_USE_FM",
#     field_mapping=None,
#     index_join_fields="NO_INDEXES"
# )


# arcpy.conversion.ExportTable(
#     in_table="main.soil_units",
#     out_table=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\main_soil_units",
#     where_clause="",
#     use_field_alias_as_name="NOT_USE_ALIAS",
#     field_mapping='code "code" true true false 2147483647 Text 0 0,First,#,main.soil_units,code,0,2147483646;soilclassification "soilclassification" true true false 2147483647 Text 0 0,First,#,main.soil_units,soilclassification,0,2147483646;mainsoilclassification "mainsoilclassification" true true false 2147483647 Text 0 0,First,#,main.soil_units,mainsoilclassification,0,2147483646;url "url" true true false 2147483647 Text 0 0,First,#,main.soil_units,url,0,2147483646',
#     sort_field=None
# )

# arcpy.conversion.ExportTable(
#     in_table="main.soilarea_soilunit",
#     out_table=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\main_soilarea_soilunit",
#     where_clause="",
#     use_field_alias_as_name="NOT_USE_ALIAS",
#     field_mapping='maparea_id "maparea_id" true true false 2147483647 Text 0 0,First,#,main.soilarea_soilunit,maparea_id,0,2147483646;soilunit_code "soilunit_code" true true false 2147483647 Text 0 0,First,#,main.soilarea_soilunit,soilunit_code,0,2147483646;soilunit_sequencenumber "soilunit_sequencenumber" true true false 8 BigInteger 0 0,First,#,main.soilarea_soilunit,soilunit_sequencenumber,-1,-1',
#     sort_field=None
# )

# arcpy.management.JoinField(
#     in_data="export_bro_selection",
#     in_field="maparea_id",
#     join_table="main_soilarea_soilunit",
#     join_field="maparea_id",
#     fields=None,
#     fm_option="NOT_USE_FM",
#     field_mapping=None,
#     index_join_fields="NO_INDEXES"
# )


# arcpy.management.JoinField(
#     in_data="export_bro_selection",
#     in_field="soilunit_code",
#     join_table="main_soil_units",
#     join_field="code",
#     fields=None,
#     fm_option="NOT_USE_FM",
#     field_mapping=None,
#     index_join_fields="NO_INDEXES"
# )


# arcpy.analysis.PairwiseClip(
#     in_features="export_bro_selection",
#     clip_features="Clip",
#     out_feature_class=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\ClipBro",
#     cluster_tolerance=None
# )


# arcpy.analysis.SpatialJoin(
#     target_features="ClipBro",
#     join_features="NV24_Oppervlaktewater_JD",
#     out_feature_class=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\ClipBro_NV24",
#     join_operation="JOIN_ONE_TO_ONE",
#     join_type="KEEP_ALL",
#     field_mapping='maparea_id "maparea_id" true true false 2147483647 Text 0 0,First,#,ClipBro,maparea_id,0,2147483646;maparea_collection "maparea_collection" true true false 2147483647 Text 0 0,First,#,ClipBro,maparea_collection,0,2147483646;beginlifespan "beginlifespan" true true false 2147483647 Text 0 0,First,#,ClipBro,beginlifespan,0,2147483646;endlifespan "endlifespan" true true false 2147483647 Text 0 0,First,#,ClipBro,endlifespan,0,2147483646;soilslope "soilslope" true true false 2147483647 Text 0 0,First,#,ClipBro,soilslope,0,2147483646;maparea_id_1 "maparea_id" true true false 2147483647 Text 0 0,First,#,ClipBro,maparea_id_1,0,2147483646;normalsoilprofile_id "normalsoilprofile_id" true true false 8 BigInteger 0 0,First,#,ClipBro,normalsoilprofile_id,-1,-1;maparea_id_12 "maparea_id" true true false 2147483647 Text 0 0,First,#,ClipBro,maparea_id_12,0,2147483646;soilunit_code "soilunit_code" true true false 2147483647 Text 0 0,First,#,ClipBro,soilunit_code,0,2147483646;soilunit_sequencenumber "soilunit_sequencenumber" true true false 8 BigInteger 0 0,First,#,ClipBro,soilunit_sequencenumber,-1,-1;code "code" true true false 2147483647 Text 0 0,First,#,ClipBro,code,0,2147483646;soilclassification "soilclassification" true true false 2147483647 Text 0 0,First,#,ClipBro,soilclassification,0,2147483646;mainsoilclassification "mainsoilclassification" true true false 2147483647 Text 0 0,First,#,ClipBro,mainsoilclassification,0,2147483646;url "url" true true false 2147483647 Text 0 0,First,#,ClipBro,url,0,2147483646;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,ClipBro,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,ClipBro,Shape_Area,-1,-1;fid_1 "fid_1" true true false 0 Double 0 0,First,#,NV24_Oppervlaktewater_JD,fid_1,-1,-1;Nvgebid "Nvgebid" true true false 80 Text 0 0,First,#,NV24_Oppervlaktewater_JD,Nvgebid,0,79;Nvklass "Nvklass" true true false 80 Text 0 0,First,#,NV24_Oppervlaktewater_JD,Nvklass,0,79;Oordeel_NV "Oordeel_NV" true true false 254 Text 0 0,First,#,NV24_Oppervlaktewater_JD,Oordeel_NV,0,253;Shape__Area "Shape__Area" false true true 0 Double 0 0,First,#,NV24_Oppervlaktewater_JD,Shape__Area,-1,-1;Shape__Length "Shape__Length" false true true 0 Double 0 0,First,#,NV24_Oppervlaktewater_JD,Shape__Length,-1,-1',
#     match_option="INTERSECT",
#     search_radius=None,
#     distance_field_name="",
#     match_fields=None
# )

# arcpy.analysis.SpatialJoin(
#     target_features="Clip",
#     join_features="ClipBro_NV24",
#     out_feature_class=r"P:\GIS Projecten\GasunieDRC\GasunieDRC.gdb\ClipBRTBro_NV24_SpatialJoin",
#     join_operation="JOIN_ONE_TO_ONE",
#     join_type="KEEP_ALL",
#     field_mapping='id "id" true true false 80 Text 0 0,First,#,Clip,id,0,79;category "category" true true false 80 Text 0 0,First,#,Clip,category,0,79;gewas "gewas" true true false 80 Text 0 0,First,#,Clip,gewas,0,79;gewascode "gewascode" true true false 4 Long 0 0,First,#,Clip,gewascode,-1,-1;jaar "jaar" true true false 4 Long 0 0,First,#,Clip,jaar,-1,-1;status "status" true true false 80 Text 0 0,First,#,Clip,status,0,79;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,Clip,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,Clip,Shape_Area,-1,-1;Join_Count "Join_Count" true true false 4 Long 0 0,First,#,ClipBro_NV24,Join_Count,-1,-1;TARGET_FID "TARGET_FID" true true false 8 BigInteger 0 0,First,#,ClipBro_NV24,TARGET_FID,-1,-1;maparea_id "maparea_id" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,maparea_id,0,2147483646;maparea_collection "maparea_collection" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,maparea_collection,0,2147483646;beginlifespan "beginlifespan" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,beginlifespan,0,2147483646;endlifespan "endlifespan" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,endlifespan,0,2147483646;soilslope "soilslope" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,soilslope,0,2147483646;maparea_id_1 "maparea_id" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,maparea_id_1,0,2147483646;normalsoilprofile_id "normalsoilprofile_id" true true false 8 BigInteger 0 0,First,#,ClipBro_NV24,normalsoilprofile_id,-1,-1;maparea_id_12 "maparea_id" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,maparea_id_12,0,2147483646;soilunit_code "soilunit_code" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,soilunit_code,0,2147483646;soilunit_sequencenumber "soilunit_sequencenumber" true true false 8 BigInteger 0 0,First,#,ClipBro_NV24,soilunit_sequencenumber,-1,-1;code "code" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,code,0,2147483646;soilclassification "soilclassification" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,soilclassification,0,2147483646;mainsoilclassification "mainsoilclassification" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,mainsoilclassification,0,2147483646;url "url" true true false 2147483647 Text 0 0,First,#,ClipBro_NV24,url,0,2147483646;fid_1 "fid_1" true true false 8 Double 0 0,First,#,ClipBro_NV24,fid_1,-1,-1;Nvgebid "Nvgebid" true true false 80 Text 0 0,First,#,ClipBro_NV24,Nvgebid,0,79;Nvklass "Nvklass" true true false 80 Text 0 0,First,#,ClipBro_NV24,Nvklass,0,79;Oordeel_NV "Oordeel_NV" true true false 254 Text 0 0,First,#,ClipBro_NV24,Oordeel_NV,0,253;Shape_Length_1 "Shape_Length" false true true 8 Double 0 0,First,#,ClipBro_NV24,Shape_Length,-1,-1;Shape_Area_1 "Shape_Area" false true true 8 Double 0 0,First,#,ClipBro_NV24,Shape_Area,-1,-1;grond_type "grond_type" true true false 512 Text 0 0,First,#,ClipBro_NV24,grond_type,0,511;nh3_calc_value "nh3_calc_value" true true false 8 Double 0 0,First,#,ClipBro_NV24,nh3_calc_value,-1,-1;hectm "hectm" true true false 8 Double 0 0,First,#,ClipBro_NV24,hectm,-1,-1',
#     match_option="LARGEST_OVERLAP",
#     search_radius=None,
#     distance_field_name="",
#     match_fields=None
# )




# arcpy.management.CalculateField(
#     in_table="ClipBRTBro_NV24_SpatialJoin",
#     field="grond_type",
#     expression="set_value(!soilclassification!)",
#     expression_type="PYTHON3",
#     code_block="""# Example: set 'NewField' to 1 if othersoilname_First matches any of these values
# def set_value(soil):
#     if soil in [
#         'Kalkarme drechtvaaggronden; zavel en lichte klei, profielverloop 1',
#         'Kalkarme poldervaaggronden; zware zavel, profielverloop 5',
#         'Kalkhoudende vlakvaaggronden; zwak en sterk lemig, kleiig, uiterst fijn zand',
#         'Kalkrijke poldervaaggronden; lichte klei, profielverloop 5',
#         'Kalkrijke poldervaaggronden; zware klei, profielverloop 5',
#         'Kalkrijke poldervaaggronden; zware zavel, profielverloop 5',
#         'Hollebollige, gemoerde zeekleigronden; zw. zavel en l. klei',
#         'Kalkrijke drechtvaaggronden; klei, profielverloop 1',
#         'Kalkrijke poldervaaggronden; lichte zavel, profielverloop 5',
#         'Kalkrijke nesvaaggronden; klei',
#         'Kalkarme nesvaaggronden; klei',
#         'Knippige poldervaaggronden; zware zavel, profielverloop 5',
#         'Knippige poldervaaggronden; zavel, profielverloop 4, of 4 en 3',
#         'Knippige poldervaaggronden; klei, profielverloop 4, of 4 en 3',
#         'Moerige eerdgronden met een zavel- of kleidek en een moerige tussenlaag op zand',
#         'Slikvaaggronden; geen zand beginnend ondieper dan 0.8 m',
#         'Kalkrijke nesvaaggronden; zware zavel',
#         'Kalkrijke poldervaaggronden; lichte zavel, profielverloop 2',
#         'Kalkarme drechtvaaggronden; zware klei, profielverloop 1',
#         'Kalkrijke poldervaaggronden; klei, profielverloop 2',
#         'Moerige eerdgronden met een moerige bovengrond of moerige tussenlaag op gerijpte zavel of klei',
#         'Kalkarme poldervaaggronden; klei, profielverloop 3, of 3 en 4, of 4',
#         'Kalkrijke poldervaaggronden; zware zavel, profielverloop 2',
#         ''
        
        
        
        
        
        
#     ]:
#         return 'klei'  # or whatever value you want to assign
#     if soil in [
#         'Veldpodzolgronden; leemarm en zwak lemig fijn zand',
#         'Laarpodzolgronden; leemarm en zwak lemig fijn zand',
#         'Kreekbeddingen',
#         'Laarpodzolgronden; lemig fijn zand',
#         'Veldpodzolgronden; lemig fijn zand',
#         'Veldpodzolgronden; leemarm en zwak lemig fijn zand',
#         'Beekeerdgronden; leemarm en zwak lemig fijn zand',
#         'Gooreerdgronden; leemarm en zwak lemig fijn zand',
#         'Gooreerdgronden; lemig fijn zand',
#         'Duinvaaggronden; leemarm en zwak lemig fijn zand',
#         'Kalkhoudende duinvaaggronden; fijn zand',
#         'Hoge zwarte enkeerdgronden; leemarm en zwak lemig fijn zand',
#         'Hoge zwarte enkeerdgronden; lemig fijn zand',
#         'Beekeerdgronden; lemig fijn zand',
#         'Vlakvaaggronden; lemig fijn zand',
#         ''
        
        
        
#     ]:
#         return 'zand'  # optional, for all others

#     if soil in [
#         'Koopveengronden op zeggeveen, rietzeggeveen of (mesotroof) broekveen',
#         'Waardveengronden op veenmosveen',


#     ]:
#         return 'veen'  # optional, for all others
# """,
#     field_type="TEXT",
#     enforce_domains="NO_ENFORCE_DOMAINS"
# )

# arcpy.management.CalculateField(
#     in_table="ClipBRTBro_NV24_SpatialJoin",
#     field="nh3_calc_value",
#     expression="set_value(!grond_type!,!Oordeel_NV!)",
#     expression_type="PYTHON3",
#     code_block="""# Example: set 'NewField' to 1 if othersoilname_First matches any of these values
# def set_value(soil, nv):
#     if soil == 'klei' and nv == "NV-gebied (stikstof en fosfor)":
#         return 29.3104  # or whatever value you want to assign
#     elif soil == 'klei' and nv == "geen NV-gebied":
#         return 32.3959  # or whatever value you want to assign
#     elif soil == 'zand' and nv == "geen NV-gebied":
#         return 29.7912  # or whatever value you want to assign
#     elif soil == 'zand' and nv == "NV-gebied (stikstof en fosfor)":
#         return 27.2267  # or whatever value you want to assign
#     elif soil == 'loss' and nv == "geen NV-gebied":
#         return 29.7912  # or whatever value you want to assign
#     elif soil == 'loss' and nv == "NV-gebied (stikstof en fosfor)":
#         return 27.2267  # or whatever value you want to assign
#     elif soil == 'veen' and nv == "geen NV-gebied":
#         return 28.9898  # or whatever value you want to assign
#     elif soil == 'veen' and nv == "NV-gebied (stikstof en fosfor)":
#         return 26.5855  # or whatever value you want to assign""",
#     field_type="DOUBLE",
#     enforce_domains="NO_ENFORCE_DOMAINS"
# )





# arcpy.management.CalculateGeometryAttributes(
#     in_features="ClipBRTBro_NV24_SpatialJoin",
#     geometry_property="hectm AREA",
#     length_unit="",
#     area_unit="HECTARES",
#     coordinate_system='PROJCS["RD_New",GEOGCS["GCS_Amersfoort",DATUM["D_Amersfoort",SPHEROID["Bessel_1841",6377397.155,299.1528128]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Double_Stereographic"],PARAMETER["False_Easting",155000.0],PARAMETER["False_Northing",463000.0],PARAMETER["Central_Meridian",5.38763888888889],PARAMETER["Scale_Factor",0.9999079],PARAMETER["Latitude_Of_Origin",52.15616055555555],UNIT["Meter",1.0]]',
#     coordinate_format="SAME_AS_INPUT"
# )


# arcpy.management.CalculateField(
#     in_table="ClipBRTBro_NV24_SpatialJoin",
#     field="nh3_calculated",
#     expression="!hectm!*!nh3_calc_value!",
#     expression_type="PYTHON3",
#     code_block="",
#     field_type="DOUBLE",
#     enforce_domains="NO_ENFORCE_DOMAINS"
# )


# arcpy.management.CalculateField(
#     in_table="ClipBRTBro_NV24_SpatialJoin",
#     field="Spreiding",
#     expression="0.3",
#     expression_type="PYTHON3",
#     code_block="",
#     field_type="DOUBLE",
#     enforce_domains="NO_ENFORCE_DOMAINS"
# )

# arcpy.management.CalculateField(
#     in_table="ClipBRTBro_NV24_SpatialJoin",
#     field="warmte",
#     expression="0",
#     expression_type="PYTHON3",
#     code_block="",
#     field_type="DOUBLE",
#     enforce_domains="NO_ENFORCE_DOMAINS"
# )


# arcpy.management.CalculateField(
#     in_table="ClipBRTBro_NV24_SpatialJoin",
#     field="hoogte",
#     expression="0.5",
#     expression_type="PYTHON3",
#     code_block="",
#     field_type="DOUBLE",
#     enforce_domains="NO_ENFORCE_DOMAINS"
# )


# arcpy.management.RepairGeometry(
#     in_features="ClipBRTBro_NV24_SpatialJoin",
#     delete_null="DELETE_NULL",
#     validation_method="ESRI"
# )





# ----------------------------------------------------------
# Gasunie DRC – BRO, BRT, NV24 processing workflow
# Fully refactored & structured ArcPy script
# Author: <you>
# ----------------------------------------------------------

import arcpy
import os
import sys
import traceback

# ----------------------------------------------------------
# SETTINGS & PARAMETERS
# ----------------------------------------------------------

arcpy.env.overwriteOutput = True

# Workspaces
PROJECT_GDB = r"C:\Users\RikdeHoop\De Essentie B.V\Gasunie - Delta Rhine Corridor quickscan Natura 2000 (GDRC) - Werkbestanden - GIS-AutoCad-FME\_GDB\GasunieDRC_actueel.gdb"
GPKG_BRO = r"C:\Users\RikdeHoop\Documents\Local_proj\ArcGIS_local_root\local_data\brobodemkaart\BRO_Bodemkaart.gpkg"
arcpy.env.workspace = PROJECT_GDB
arcpy.env.overwriteOutput = True
arcpy.env.scratchWorkspace = arcpy.env.scratchGDB

# ----------------------------------------------------------
# Input datasets
# ----------------------------------------------------------

# GeoPackage (BRO bodemkaart)


# BRO layers inside the GPKG
FC_SOILAREA = os.path.join(GPKG_BRO, "main", "soilarea")
TBL_SOILPROFILE = os.path.join(GPKG_BRO, "main", "soilarea_normalsoilprofile")
TBL_SOILUNITS = os.path.join(GPKG_BRO, "main", "soil_units")
TBL_SOILAREA_UNIT = os.path.join(GPKG_BRO, "main", "soilarea_soilunit")

# Other input datasets stored in GDB or elsewhere
FC_BRPPER = "brpgewaspercelen"
FC_PIPE = "DRC_Hartlijn_leidingen_West"
# NV24 is an ArcGIS Online Feature Service
FC_NV24 = "NV24_Oppervlaktewater_JD"



# Important projection (RD New)
RD_NEW = (
    'PROJCS["RD_New",GEOGCS["GCS_Amersfoort",'
    'DATUM["D_Amersfoort",SPHEROID["Bessel_1841",6377397.155,299.1528128]],'
    'PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],'
    'PROJECTION["Double_Stereographic"],'
    'PARAMETER["False_Easting",155000.0],'
    'PARAMETER["False_Northing",463000.0],'
    'PARAMETER["Central_Meridian",5.38763888888889],'
    'PARAMETER["Scale_Factor",0.9999079],'
    'PARAMETER["Latitude_Of_Origin",52.15616055555555],'
    'UNIT["Meter",1.0]]'
)

# ----------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------

def safe_run(func, description):
    """Runs a function with error handling."""
    try:
        arcpy.AddMessage(f"➡ {description}")
        func()
        arcpy.AddMessage(f"✔ Completed: {description}")
    except Exception as e:
        arcpy.AddError(f"❌ ERROR in {description}: {str(e)}")
        traceback.print_exc()
        sys.exit(1)


# ----------------------------------------------------------
# 1. PREPARATION: PROJECTION + BUFFER + CLIP
# ----------------------------------------------------------

def prepare_datasets():
    """Define projection, buffer pipeline, and clip BRP."""

    # Define projection
    arcpy.management.DefineProjection(FC_BRPPER, RD_NEW)

    # Buffer pipeline
    buffer_fc = os.path.join(PROJECT_GDB, "buffer")
    arcpy.analysis.Buffer(
        FC_PIPE, buffer_fc, "20 Meters",
        line_side="FULL", line_end_type="ROUND",
        dissolve_option="NONE"
    )

    # Clip BRP by buffer  
    clip_fc = os.path.join(PROJECT_GDB, "Clip")
    arcpy.analysis.PairwiseClip(FC_BRPPER, buffer_fc, clip_fc)

    return buffer_fc, clip_fc


# ----------------------------------------------------------
# 2. SELECT SOIL AREA + EXPORT
# ----------------------------------------------------------

def select_and_export_soilareas(clip_fc):
    """Select soil areas intersecting with clip region."""
    arcpy.management.SelectLayerByLocation(
        FC_SOILAREA, "INTERSECT", clip_fc
    )

    export_fc = os.path.join(PROJECT_GDB, "export_bro_selection")

    arcpy.conversion.ExportFeatures(FC_SOILAREA, export_fc)

    return export_fc


# ----------------------------------------------------------
# 3. PROCESS SOIL PROFILE TABLES
# ----------------------------------------------------------

def export_and_join_tables(export_fc):
    """Exports relevant supporting tables & performs joins."""

    # Export supporting tables
    soilprof_tbl = os.path.join(PROJECT_GDB, "soilprofile_export")
    soilunits_tbl = os.path.join(PROJECT_GDB, "soilunits_export")
    soilareaunit_tbl = os.path.join(PROJECT_GDB, "soilareaunit_export")

    arcpy.conversion.ExportTable(TBL_SOILPROFILE, soilprof_tbl)
    arcpy.conversion.ExportTable(TBL_SOILUNITS, soilunits_tbl)
    arcpy.conversion.ExportTable(TBL_SOILAREA_UNIT, soilareaunit_tbl)

    # Join soilprofiles
    arcpy.management.JoinField(
        export_fc, "maparea_id",
        soilprof_tbl, "maparea_id"
    )

    # Join soilarea_soilunit
    arcpy.management.JoinField(
        export_fc, "maparea_id",
        soilareaunit_tbl, "maparea_id"
    )

    # Join soil unit attributes
    arcpy.management.JoinField(
        export_fc, "soilunit_code",
        soilunits_tbl, "code"
    )

    return export_fc


# ----------------------------------------------------------
# 4. SECOND CLIP + JOIN WITH NV24
# ----------------------------------------------------------

def enrich_with_nv24(export_fc, clip_fc):
    """Clip BRO selection again & perform NV24 spatial joins."""

    clip_bro = os.path.join(PROJECT_GDB, "ClipBro")
    arcpy.analysis.PairwiseClip(export_fc, clip_fc, clip_bro)

    # Spatial join BRO with NV24
    bro_nv = os.path.join(PROJECT_GDB, "ClipBro_NV24")
    arcpy.analysis.SpatialJoin(
        clip_bro, FC_NV24, bro_nv,
        match_option="INTERSECT"
    )

    # Spatial join with BRP clip
    final_join = os.path.join(PROJECT_GDB, "ClipBRTBro_NV24_SpatialJoin")
    arcpy.analysis.SpatialJoin(
        clip_fc, bro_nv, final_join,
        match_option="LARGEST_OVERLAP"
    )

    return final_join


# ---------------------------------------------------------- #
# 5. FIELD CALCULATIONS (grond_type, NH3 etc.)
# ---------------------------------------------------------- #
def calculate_fields(final_fc):
    """Calculate grond_type, NH3, hectare area, and other fields."""

    # grond_type
    arcpy.management.CalculateField(
        final_fc,
        "grond_type",
        "set_value(!soilclassification!)",
        "PYTHON3",
        code_block="""
def set_value(soil):
    klei = [
        'Kalkarme drechtvaaggronden; zavel en lichte klei, profielverloop 1',
        'Kalkarme poldervaaggronden; zware zavel, profielverloop 5',
        'Kalkhoudende vlakvaaggronden; zwak en sterk lemig, kleiig, uiterst fijn zand',
        'Kalkrijke poldervaaggronden; lichte klei, profielverloop 5',
        'Kalkrijke poldervaaggronden; zware klei, profielverloop 5',
        'Kalkrijke poldervaaggronden; zware zavel, profielverloop 5',
        'Hollebollige, gemoerde zeekleigronden; zw. zavel en l. klei',
        'Kalkrijke drechtvaaggronden; klei, profielverloop 1',
        'Kalkrijke poldervaaggronden; lichte zavel, profielverloop 5',
        'Kalkrijke nesvaaggronden; klei',
        'Kalkarme nesvaaggronden; klei',
        'Knippige poldervaaggronden; zware zavel, profielverloop 5',
        'Knippige poldervaaggronden; zavel, profielverloop 4, of 4 en 3',
        'Knippige poldervaaggronden; klei, profielverloop 4, of 4 en 3',
        'Moerige eerdgronden met een zavel- of kleidek en een moerige tussenlaag op zand',
        'Slikvaaggronden; geen zand beginnend ondieper dan 0.8 m',
        'Kalkrijke nesvaaggronden; zware zavel',
        'Kalkrijke poldervaaggronden; lichte zavel, profielverloop 2',
        'Kalkarme drechtvaaggronden; zware klei, profielverloop 1',
        'Kalkrijke poldervaaggronden; klei, profielverloop 2',
        'Moerige eerdgronden met een moerige bovengrond of moerige tussenlaag op gerijpte zavel of klei',
        'Kalkarme poldervaaggronden; klei, profielverloop 3, of 3 en 4, of 4',
        'Kalkrijke poldervaaggronden; zware zavel, profielverloop 2',
        'Geëgaliseerde en verwerkte zeekleigronden met plaats. veen binnen 1.2 m; klei',
        'Geëgaliseerde en verwerkte zeekleigronden zonder veen binnen 1.2 m; zw. zavel en l. klei',
        'Hollebollige, gemoerde zeekleigronden; zw. zavel en l. klei',
        'Kalkarme poldervaaggronden; zavel, profielverloop 3, of 3 en 4, of 4',
        'Kalkarme poldervaaggronden; lichte zavel, profielverloop 5'

        
    ]
    zand = [
        'Veldpodzolgronden; leemarm en zwak lemig fijn zand',
        'Laarpodzolgronden; leemarm en zwak lemig fijn zand',
        'Kreekbeddingen',
        'Laarpodzolgronden; lemig fijn zand',
        'Veldpodzolgronden; lemig fijn zand',
        'Beekeerdgronden; leemarm en zwak lemig fijn zand',
        'Gooreerdgronden; leemarm en zwak lemig fijn zand',
        'Gooreerdgronden; lemig fijn zand',
        'Duinvaaggronden; leemarm en zwak lemig fijn zand',
        'Kalkhoudende duinvaaggronden; fijn zand',
        'Kalkhoudende vlakvaaggronden; zeer fijn zand',
        'Hoge zwarte enkeerdgronden; leemarm en zwak lemig fijn zand',
        'Hoge zwarte enkeerdgronden; lemig fijn zand',
        'Beekeerdgronden; lemig fijn zand',
        'Vlakvaaggronden; lemig fijn zand'
    ]
    veen = [
        'Koopveengronden op zeggeveen, rietzeggeveen of (mesotroof) broekveen',
        'Waardveengronden op veenmosveen'
    ]

    if soil in klei: return 'klei'
    if soil in zand: return 'zand'
    if soil in veen: return 'veen'
"""
    )

    # NH3 base values
    arcpy.management.CalculateField(
        in_table=final_fc,
        field="nh3_calc_value",
        expression="set_value(!grond_type!,!Oordeel_NV!)",
        expression_type="PYTHON3",
        code_block="""
def set_value(soil, nv):
    if soil == 'klei' and nv == "NV-gebied (stikstof en fosfor)":
        return 29.3104
    elif soil == 'klei' and nv == "geen NV-gebied":
        return 32.3959
    elif soil == 'zand' and nv == "geen NV-gebied":
        return 29.7912
    elif soil == 'zand' and nv == "NV-gebied (stikstof en fosfor)":
        return 27.2267
    elif soil == 'loss' and nv == "geen NV-gebied":
        return 29.7912
    elif soil == 'loss' and nv == "NV-gebied (stikstof en fosfor)":
        return 27.2267
    elif soil == 'veen' and nv == "geen NV-gebied":
        return 28.9898
    elif soil == 'veen' and nv == "NV-gebied (stikstof en fosfor)":
        return 26.5855
"""
        ,
        field_type="DOUBLE",
        enforce_domains="NO_ENFORCE_DOMAINS"
    )

    fin_out_ = os.path.join(PROJECT_GDB, "ClipBRTBro_NV24_vauto")

    arcpy.management.MultipartToSinglepart(
        final_fc,
        out_feature_class=fin_out_ 
    )

    final_fc = fin_out_ 

    # Area in hectares
    arcpy.management.CalculateGeometryAttributes(
        final_fc,
        geometry_property="hectm AREA",
        area_unit="HECTARES",
        coordinate_system=RD_NEW
    )

    final_fc   # your feature class

    with arcpy.da.UpdateCursor(final_fc, ["hectm"]) as cursor:
        for row in cursor:
            if row[0] < 0.005:
                cursor.deleteRow()

    arcpy.management.AddField(
        final_fc,
        "nh3_calculated",
        "DOUBLE"
    )
    # Final NH3 multiplied
    arcpy.management.CalculateField(
        final_fc, "nh3_calculated",
        "!hectm! * !nh3_calc_value!",
        "PYTHON3"
    )
    arcpy.management.AddField(
        final_fc,
        "hoogte",
        "DOUBLE"
    )
    arcpy.management.AddField(
        final_fc,
        "warmte",
        "DOUBLE"
    )    
    arcpy.management.AddField(
        final_fc,
        "spreiding",
        "DOUBLE"
    )
    # Fixed fields
    arcpy.management.CalculateField(final_fc, "spreiding", "0.3")
    arcpy.management.CalculateField(final_fc, "warmte", "0")
    arcpy.management.CalculateField(final_fc, "hoogte", "0.5")



# ----------------------------------------------------------
# 6. CLEAN GEOMETRY + EXPORT
# ----------------------------------------------------------

def finalize(final_fc):
    """Repair geometry and force singlepart output."""
    # arcpy.management.RepairGeometry(final_fc, delete_null='DELETE_NULL', validation_method='ESRI')
    # arcpy.management.RepairGeometry(final_fc, delete_null='DELETE_NULL', validation_method='OGC')
    out_ = os.path.join(PROJECT_GDB, "ClipBRTBro_NV24SP_vauto")

    # Save the multipart feature class (NO singlepart conversion)
    arcpy.management.CopyFeatures(final_fc, out_)

    return out_



# ----------------------------------------------------------
# MAIN WORKFLOW
# ----------------------------------------------------------

def main():
    safe_run(
        lambda: prepare_datasets(),
        "Prepare datasets: projection, buffer, clip"
    )

    buffer_fc, clip_fc = prepare_datasets()

    safe_run(
        lambda: select_and_export_soilareas(clip_fc),
        "Select soilareas & export"
    )

    export_fc = select_and_export_soilareas(clip_fc)

    safe_run(
        lambda: export_and_join_tables(export_fc),
        "Export & join soil profile tables"
    )

    joined_fc = export_and_join_tables(export_fc)

    safe_run(
        lambda: enrich_with_nv24(joined_fc, clip_fc),
        "Perform NV24 spatial joins"
    )

    final_fc = enrich_with_nv24(joined_fc, clip_fc)

    safe_run(
        lambda: calculate_fields(final_fc),
        "Calculate derived fields (grond_type, NH3, area, etc.)"
    )

    safe_run(
        lambda: finalize(final_fc),
        "Repair geometry & export singlepart"
    )


# ----------------------------------------------------------
# RUN SCRIPT
# ----------------------------------------------------------

if __name__ == "__main__":
    main()

