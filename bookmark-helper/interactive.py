#!/bin/python
import sys

targetFile = open("/home/user/.config/homepage.html","r")
targetText = targetFile.readlines()
targetFile.close()

# handles seting state, defalt state is 1
if len(sys.argv) >= 1:
    state = int(sys.argv[1])
else:
    state = 1
if state < 2:
    print("title")
    title = input()
    if state == 1:
        print("addr")
        addr = input()
# state
# 0 appends a section to the page
# 1 appends a link to the end of the selected section
# 2 edit mode? lets you remove bookmarks by section TODO


def appendLink(title,addr):
    return "    <p>"+title+"\n      <a href='"+addr+"'>"+addr+"</a></p>\n"
def appendSection(title):
    return "<h1>"+title+"</h1>\n"

sectionList = []
sectionListLine = []
for i in range(1,len(targetText)):
    line = targetText[i]
    if line[1]+line[2] == "h1":
        line = line.replace("</h1>\n","")
        line = line.replace("<h1>","")
        sectionList.append(line)
        sectionListLine.append(i)
print(sectionList)
print(sectionListLine)

#sets target section
if state != 0:
    sectionReturnString = ""
    for i in range(0,len(sectionList)):
        sectionReturnString = sectionReturnString + sectionList[i] + " - " + str(i) + "\n"
    print(sectionReturnString)
    targetSection = int(input())

if state == 0:
    targetText.insert(len(targetText)-2,appendSection(title))
    print(appendSection(title))
elif state == 1:
    if targetSection>= len(sectionListLine)-1:
        targetText.insert(len(targetText)-2,appendLink(title,addr))
    else:
        targetText.insert(sectionListLine[targetSection+1],appendLink(title,addr))
    print(appendLink(title,addr))
## WIP LINK REMOVER
elif state == 2:
    linkList = []
    linkListLine = []
    if targetSection >= len(sectionListLine)-1:
        endLine = len(targetText)-2
    else:
        endLine = sectionListLine[targetSection+1]
    startLine = sectionListLine[targetSection]
    for i in range(startLine,endLine):
        line = targetText[i]
        if line[4]+line[5]+line[6] == "<p>":
            line = line.replace("<p>","")
            line = line.replace("\n","")
            linkList.append(line)
            linkListLine.append(i)
    print(linkList)
    linkReturn = ""
    for i in range(0,len(linkList)):
        linkReturn = linkReturn + linkList[i] + " - " + str(i) + "\n"
    print(linkReturn)
    targetLink = int(input())
    del targetText[linkListLine[targetLink]+1]
    del targetText[linkListLine[targetLink]]
targetFile = open("/home/user/.config/homepage.html","w")
for text in targetText:
    targetFile.write(text)
  
