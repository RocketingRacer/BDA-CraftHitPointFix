#Rocketing Racer
#RocketingRacer@gmail.com
#dec 18 2018
#How To Use:
#place script in folder of craft files to be fixed
import os
import glob
def main():
    #partfilename = input("Name of part Reference file: ")
    dirName = 'fixed'
    logfile = open("Log.jra",'w')
    try:
        os.mkdir(dirName)
        print("Directory" , dirName ,  "Created ")
    except FileExistsError:
        print("Directory", dirName ,  "already exists")
    crafts = []
    partDict = {}
    for partfilename in glob.glob("*.csv"):
        print("File Imported: " +partfilename)
        inputFile = open(partfilename)
        while True:
            try:
                part = inputFile.readline().split(",")
                if len(part)<4:
                    partDict[part[0]] = [int(part[1]),"Never"]
                    print("ExplodeMode Not Found for Part:", part[0])
                else:
                    partDict[part[0]] = [int(part[1]),part[2]]
            except:
                break
        inputFile.close()
    if len(partDict) ==0:
        logfile.write("Error No CSV files Detected\n")
        input("Error No CSV files Detected (Press enter to exit)")
        return 0
    else:
        print("Found", len(partDict), "Parts to be changed")

    for file in glob.glob("*.craft"):
        crafts.append(file)
    fileQueue = crafts
    changes = 0
    if len(fileQueue)==0:
        input("Error No Craft files Detected (Press enter to exit)")
        return 0
    else:
        print("Found", len(fileQueue), "Craft Files")
    for problemFile in fileQueue:
        print("Editing File: "+problemFile)
        inputFile = open(problemFile)
        outputFileName = "fixed/"+problemFile
        writeFile = open(outputFileName, 'w')
        fileContents = inputFile.read()
        fileLines = fileContents.split('\n')
        currentPart = ''
        issue = False
        for line in fileLines:
            if "part =" in line:
                currentPart = line.split(' ')[2]
                currentPart =currentPart.split('_')[0]
                try:
                    x = partDict[currentPart]
                    issue=True
                    changes+=1
                    output = ("\tPart detected with issue: " + currentPart)
                    print(output+" on "+problemFile)
                    logfile.write(output+" IN FILE ("+problemFile+')\n')
                except:
                    issue=False
            if issue == True:
                if "Hitpoints =" in line:
                    pref,old = prefixMake(line)
                    line =  pref + str(partDict[currentPart][0])
                    #print("\t\tHitpoints changed! "+old+" -->",(partDict[currentPart])[0])
                if "maxHitPoints =" in line:
                    pref,old = prefixMake(line)
                    line =  pref + str(partDict[currentPart][0])
                    #print("\t\tmaxHitPoints changed! "+old+" -->",(partDict[currentPart])[0])
                if "ExplodeMode =" in line:
                    pref,old = prefixMake(line)
                    line =  pref + str(partDict[currentPart][1])
                    #print("\t\tExplodeMode Changed! "+old+" -->",(partDict[currentPart])[1])
                    #print(line)
            writeFile.write(line+'\n')
        writeFile.close()
    input(str("Made "+str(changes)+" changes to craft files! (Press Enter to Close)"))
    return 0
def prefixMake(line):
    old = line.split(' ')[-1]
    lineData = line.split(' ')[0:-1]
    pref = ''
    for linepart in lineData:
        pref += linepart+' '
    return pref,old
if __name__ == "__main__":
    main()
