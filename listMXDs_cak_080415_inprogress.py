#-------------------------------------------------------------
# Name:       listMXDs_cak_080415.py
# Purpose:    
# Author:     TDOT/cakraemer
# Created:    04/08/2015
# Copyright:   
# ArcGIS Version:   10.3.1
# Python Version:   2.7
#-------------------------------------------------------------

import arcpy, os

#Get xlsxwriter: http://xlsxwriter.readthedocs.org/en/latest/index.html
import xlsxwriter

##This section is for variables
#These need to be arguments
inputdir = r"F:\testing_ground\data_connections_SEMS"
outputdir = r"F:\My_Stuff\Python\Tscripts\junk"

#Isolates folder name in directory path
fname = os.path.basename(workspace)

#Creates Excel workbook
wrkbook = xlsxwriter.Workbook(outputdir + '\\' + fname + '.xlsx') 

#Creates list of MXDs found in input directory
mxdsList = []

##This section will walk through the workspace directory and add all mxds to a list
for root, dirs, files in os.walk(inputdir):
    for f in files:
        if f.endswith(".mxd"):
            mxd = root + '\\' + f
            mxdsList.append(mxd)

print(mxdsList)

##Create a separate worksheet in the Excel workbook for each MXD
