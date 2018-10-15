##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: megan.ossmann@duke.edu(for ENV859)
##---------------------------------------------------------------------

#import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

#construct a while loop to iterate through all lines in datafile

#open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

#get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()
while lineString:
    #set code to run only if the line contains "Date :"
    if "Date :" in lineString:

        #parse the line string into a list
        lineList = lineString.split()
        
        #extract attributes from the datum header line
        tagID = lineList[0]

        #get the next line
        line2String = inputFileObj.readline()

        #parse the line into a list
        line2Data = line2String.split()

        #get attributes from second line
        obsLat = line2Data[2]
        obsLon = line2Data[5]
        print(tagID, obsLat, obsLon)
        

    #Get the next line
    lineString = inputFileObj.readline()
    
#close the file object
inputFileObj.close()

    