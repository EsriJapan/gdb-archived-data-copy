#
# coding:utf-8
#-------------------------------------------------------------------------------
# Name:        gdbTimedDataCopy.py
# Purpose:     export shapefile data from selectied time in geodatabase
#
# Author:      ej2217
#
# Created:     10/06/2015
# Copyright:   (c) ej2217 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import arcpy

input_list = sys.argv[1:]

#########create database connection############

print(input_list)

#Create database connection
arcpy.CreateDatabaseConnection_management(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4], input_list[5], input_list[6], input_list[7], input_list[8], input_list[9], input_list[10], input_list[11], input_list[12])

###########copy############################

#local variables for feature class name
fileName = input_list[14]

#join function to get path for specific feature class in geodatabase
copy_shp ="\\".join([input_list[0], input_list[1] + ".sde", fileName]);

#check the path name
print(copy_shp)

##saving place for .shp, which is same as where you created database connection
tool_test_folder = input_list[0]

# Process:(Feature Class To Shapefile (multiple))
# this time I use only (single)
arcpy.FeatureClassToShapefile_conversion(copy_shp, tool_test_folder)


