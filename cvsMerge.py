#Rocketing Racer
#RocketingRacer@gmail.com
#Dec 19 2018
import glob
try:
    mergedFile = open("mergedCSV.csv",'a')
    print("Appending to Merged CSV")
except:
    mergedFile = open("mergedCSV.csv",'w')
    print("Creating Merged CSV")
for file in glob.glob("*.csv"):
    readingFile = open(file)
    string=readingFile.read()
    readingFile.close()
    mergedFile.write(string)
mergedFile.close()
