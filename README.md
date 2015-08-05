# listDataConnectionsMXD
Python script(s) for listing data connections of layers in an ArcGIS MXD.

#Purpose

This will likely turn into a collection of scripts that are to be used with ArcGIS Desktop. I'm getting my feet wet in GitHub and attempting to write more python scripts, particularly those using arcpy. I'd love to learn more so please comment with suggestions. In return, you are welcome to take what you need. Let me know if it helps you! Thank you in advance!

#List of scripts in listDataConnectionsMXD by date submitted
(Newest on top)

##08.04.15

arcpy_data_connections_cak_080415.py

###For ArcToolbox

####Title  Data Connections in MXD

####Summary
Python script for listing data connections of layers in an MXD. This will break down the layers by dataframe and feature layer type. The output is a CSV file that the user defines.

####Syntax
dataConnectionsMXD (MXD, Output_CSV_File) 

Parameter|Explanation Data|Type 
---------|----------------|----
MXD|Dialog Reference|ArcMap Document

                                  Select an MXD that you would like to analyze 
                                  and create a list of feature, raster, service, 
                                  and table view connections.

                                  There is no python reference for this parameter.
  
Output_CSV_File...................Dialog Reference..................................File

                                  Navigate to a directory to store the data 
                                  connections CSV file. When naming the CSV file, 
                                  make sure to add the extension (*.csv).

                                  There is no python reference for this parameter.
  


