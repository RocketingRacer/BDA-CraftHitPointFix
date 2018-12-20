# Module Manager Config Writer
# For correcting Hitpoint and ExplodeMode values
# Use with:
# ***filename*** To generate name, hp, title  fom a laucnhed craft file.
#    (Requires KRPC be installed)
# Rocketing Racer's ***filename*** to correct existing .craft files.
# 2018.12.15 by FleshJeb - No license. Do whatever you want.
# How To Use:
# Place script in folder of input files to be converted to CFG.
# Input files have the format KSP_name, BDA_maxHitPoints, BDA_ExplodeMode, KSP_title

#inputFile format example (as .CSV file)
'''
109Prop,2000,Never,"KB 601 ""Tornado"" Engine"
herculesprop,2000,Never,"RR K56 ""Titan"" Turboprop Engine"
spitfiremerlin,2000,Never,"RR ""Kraken"" Engine"
'''

#outputfile format example (as Module Manager .CFG)
'''
@PART[spitfiremerlin] { //Kraken
    %MODULE[HitpointTracker] {
        ArmorThickness = 10
        maxHitPoints = 2000
        ExplodeMode = Never
    }

}
'''

import os
import glob

outputFileName = "000000_HitpointModule_PartFixes-AirplanePlus.cfg"
outputFile = open(outputFileName, 'w')

for inputFileName in glob.glob("*.csv"):
    inputFile = open(inputFileName,'r')
    #outputFile = open(inputFileName.split('.')[0]+".cfg", 'w')
    outputFile.write("// SOURCE: "+inputFileName+'\n')
    outputFile.write("// ADD SECTION DESCRIPTION HERE"+'\n')
    while True:
        try:
            name, hp, xplod, title = inputFile.readline().split(",")
            outputFile.write("@PART["+name+"] { // "+title.rstrip()+'\n')
            outputFile.write("\t%MODULE[HitpointTracker] {\n")
            outputFile.write("\t\tArmorThickness = 10\n")
            outputFile.write("\t\tmaxHitPoints = "+hp+'\n')
            outputFile.write("\t\tExplodeMode = "+xplod+'\n')
            outputFile.write("\t}\n")
            outputFile.write("}\n\n")
        except:
            break
    print(inputFile.name)
    #outputFile.close()
    inputFile.close()
outputFile.close()
print()
print("Converted to: "+outputFileName)
