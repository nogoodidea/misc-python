#!/bin/python
import sys,os
from newlinebegone import nlbg

## checks for file input are argv
if len(sys.argv) < 3:
    print("ERROR: needs file and output premiter")
    sys.exit()
targetFile = sys.argv[1]
outputFile = sys.argv[2]
## checks if target is a file
if os.path.isfile(targetFile) == False:
    print("ERROR: target file must exsit")
if os.path.isfile(targetFile) == False:
    print("ERROR: output file must exsit")
targetText = open(targetFile,'r').readlines()
#checks if the file is blank
if len(targetText) == 0:
    print("ERROR: target file needs text to parse")
## all good start to loop

pageNumber = int(0)
line = int(0)
activeTag = -1
firstTagRun = False
tagList = ["title","h1","left","right","blockquote","justify"]
#-1 no active tag
#0 title
#1 header
#2 left
#3 right
#4 blockquote
#5 justify

TITLE = 0
HEADER = 1
LEFT = 2
RIGHT = 3
BLOCKQUOTE = 4
JUSTIFY = 5

#first pass to keep lines within 70 caricters and to split lines
for line in range(0,len(targetText)):
    targetLine = nlbg(targetText[line])
    if len(targetLine) >= 70:
        splitList = targetLine.split(" ")
        targetLine = ""
        splitLoop = 1
        splitInt = 0
        trueLine = ""
        for i in range(0,len(splitList)):
            splitInt = splitInt + len(splitList[i])+1
            if splitInt > 70:
                if splitLoop == 1:
                    trueLine = targetLine
                else:
                    targetLine = targetLine
                    targetText.insert(line+splitLoop,targetLine)
                splitLoop = splitLoop + 1
                splitInt = 0
                targetLine = splitList[i]
            else:
                targetLine = targetLine + " " + splitList[i]
        targetLine = trueLine
        targetText[line] = targetLine
    print(targetLine)

print(targetText)
while line <=  len(targetText)-1:
    targetLine = nlbg(targetText[line])
    if line == 60 * pageNumber:
        pageNumber == pageNumber +1
        for i in range(1,3):
            targetText.insert(line+i,"")
    #tag end checker, to stop fromating the tags with activeTag and breaking things. i know if the file is mallformated it will break and the fix is trival, :)
    if targetLine.strip() == '</'+tagList[activeTag]+'>':
        if activeTag == HEADER:
            targetLine = ""
            for i in range(0,70):
                targetLine = targetLine +"-" 
            targetText.insert(line+1,"")
        elif activeTag == JUSTIFY:
            targetText.insert(line+1,"")
        activeTag = -1
        #var to stop things breaking on multiline tags
        firstTagRun == False
        targetLine = ""
    #active tag runner
    if activeTag == TITLE:
        #works due to tag parseing code
        targetLine = targetLine.upper()
        if firstTagRun == False:
            firstTagRun = True
            targetText.insert(line+2,"\n")
    elif activeTag == HEADER:
        if firstTagRun == False:
            targetText[line-1] = len(targetLine)*"-"+"\n"
    elif activeTag == LEFT:
        if firstTagRun == False:
            targetLine == "    " + targetLine
        if targetLine != "":
            targetText.insert(line+1,"")
    elif activeTag == RIGHT:
        if targetLine != "":
            targetText.insert(line+1,"")
    elif activeTag == BLOCKQUOTE:
        #hate how this works, but it should work
        if len(targetLine) >= 60:
            splitList = targetLine.split(" ")
            targetLine = ""
            splitLoop = 1
            splitInt = 0
            for i in range(0,len(splitList)):
                splitInt = splitInt + len(splitList[i])+1
                if splitInt > 60:
                    trueLine = targetLine 
                    targetLine = splitList[i]
                else:
                    targetLine = targetLine + " " + splitList[i]
            targetText[line+1] = targetLine + targetText[line+1]
            targetLine = trueLine    
            targetLine = "     " + targetLine + "     "
            
    elif activeTag == JUSTIFY:
        #todo add this 
        print("YOU NEED TO ADD THIS TAG")

    #tag checker block
    for tag in range(0,len(tagList)):
        if targetLine.strip() == "<"+tagList[tag]+">":
            activeTag = tag
            targetLine = ""
            print(tagList)
    
    #replace line from the list
    targetLine = "     " +targetLine + "     \n"
    targetText[line] = targetLine
    #loop var
    line = line + 1 

print(targetText)

output = open(outputFile,"w")
for i in range(0,len(targetText)):
    output.write(targetText[i])
output.close()
    




