#-------------------------------------------------------------
# Name:       ArcGIS_data_connections_to_CSV_cak_080315.py
# Purpose:    creates a list of data connections for layers in an MXD (for ArcToolbox)
# Author:     geoCAK
# Created:    03/08/2015
# Copyright:   
# ArcGIS Version:   10.3.1
# Python Version:   2.7
#-------------------------------------------------------------

import arcpy, os, sys, csv

##This section is for variables
mxd = arcpy.mapping.MapDocument(arcpy.GetParameterAsText(0))
csvfile = arcpy.GetParameterAsText(1)
dataframes = arcpy.mapping.ListDataFrames(mxd)

##This section states the name and path of MXD
print("MXD location and name: " + (mxd.filePath) + "\n")

#Write MXD name and path to CSV
with open(csvfile, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["MXD location and name: ", (mxd.filePath)])
    writer.writerow([])

##This section lists layers by dataframe and layer types in MXD

print("**FEATURE LAYERS**")

#Write feature layers by dataframe to CSV
with open(csvfile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow(["**FEATURE LAYERS**"])

for dataframe in dataframes:
    if dataframe in dataframes:
        print("--- Dataframe name:  " + dataframe.name + " ---")
        with open(csvfile, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(["--- Dataframe name: " + (dataframe.name + " ---")])
            writer.writerow(["Layer Name", "Data Source", "Service Properties"])
        for layer in arcpy.mapping.ListLayers(mxd, "", dataframe):
            if layer.supports("SERVICEPROPERTIES") and layer.isFeatureLayer:
                servProp = layer.serviceProperties
                print(layer.name + ", " + layer.dataSource + ", " + layer.serviceProperties.get('Service', 'N/A'))
                with open(csvfile, 'ab') as f:
                    writer = csv.writer(f)
                    writer.writerow([layer.name, layer.dataSource, (layer.serviceProperties.get('Service', 'N/A'))])
            else:
                if layer.isFeatureLayer:
                    print(layer.name + ", " + layer.dataSource)
                    with open(csvfile, 'ab') as f:
                        writer = csv.writer(f)
                        writer.writerow([layer.name, layer.dataSource])

#Creates a blank row as a separator between layer types for easier reading
with open(csvfile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow([])              

print("\n"+ "**RASTER LAYERS**")

#Write raster layers by dataframe to CSV
with open(csvfile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow(["**RASTER LAYERS**"])
    
for dataframe in dataframes:
    if dataframe in dataframes:
        print("--- Dataframe name: " + dataframe.name + " ---")
        with open(csvfile, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(["--- Dataframe name:  " + (dataframe.name + " ---")])
            writer.writerow(["Layer Name", "Data Source", "Service Properties"])
        for layer in arcpy.mapping.ListLayers(mxd, "", dataframe):
            if layer.supports("SERVICEPROPERTIES") and layer.isRasterLayer:
                servProp = layer.serviceProperties
                print(layer.name + ", " + layer.dataSource + ", " + layer.serviceProperties.get('Service', 'N/A'))
                with open(csvfile, 'ab') as f:
                    writer = csv.writer(f)
                    writer.writerow([layer.name, layer.dataSource, (layer.serviceProperties.get('Service', 'N/A'))])
            else:
                if layer.isRasterLayer:
                    print(layer.name + ", " + layer.dataSource)
                    with open(csvfile, 'ab') as f:
                        writer = csv.writer(f)
                        writer.writerow([layer.name, layer.dataSource])

#Creates a blank row as a separator between layer types for easier reading
with open(csvfile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow([])

print("\n"+ "**SERVICE LAYERS**")

#Write service layers by dataframe to CSV
with open(csvfile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow(["**SERVICE LAYERS**"])
    
for dataframe in dataframes:
    if dataframe in dataframes:
        print("--- Dataframe name: " + dataframe.name + " ---")
        with open(csvfile, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(["--- Dataframe name:  " + (dataframe.name + " ---")])
            writer.writerow(["Layer Name", "Service Type", "URL", "User Name", "Password"])
        for layer in arcpy.mapping.ListLayers(mxd, "", dataframe):
            if layer.supports("SERVICEPROPERTIES"):
                    servProp = layer.serviceProperties
                    if layer.serviceProperties["ServiceType"] != "SDE":
                        print(layer.longName + ", " + servProp.get('ServiceType', 'N/A')) + ", " + servProp.get('URL', 'N/A') + ", " + servProp.get('UserName', 'N/A') + ", " + servProp.get('Password', 'N/A')
                        with open(csvfile, 'ab') as f:
                            writer = csv.writer(f)
                            writer.writerow([layer.longName, (servProp.get('ServiceType', 'N/A')), (servProp.get('URL', 'N/A')),(servProp.get('UserName', 'N/A')), (servProp.get('Password', 'N/A'))])

#Creates a blank row as a separator between layer types for easier reading
with open(csvfile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow([])

##This section lists table views by dataframe and type in MXD

tables = arcpy.ListTables(mxd)

print("\n"+ "**TABLE VIEWS IN DIRECTORIES**")

#Write table views by dataframe to CSV
with open(csvfile, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow(["**TABLE VIEWS IN DIRECTORIES**"])

for dataframe in dataframes:
    if dataframe in dataframes:
        print("--- Dataframe name: " + dataframe.name + " ---")
        with open(csvfile, 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(["--- Dataframe name:  " + (dataframe.name + " ---")])
            writer.writerow(["Table View Name", "Data Source"])
        for table in arcpy.mapping.ListTableViews(mxd, "", dataframe):
            print "{0}, {1}".format(table.name, table.dataSource)
            with open(csvfile, 'ab') as f:
                        writer = csv.writer(f)
                        writer.writerow([table.name, table.dataSource])
                        


