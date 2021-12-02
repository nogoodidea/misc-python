#!/bin/python
import sys

# handles seting state, defalt state is 1
print(sys.argv)
if len(sys.argv) == 1:
    state = "HELP"
else:
    state = upper(sys.argv[1])
if state == "HELP":
    print("interactive.py [COMMAND] FILE NAME\nAPPEND appends section to end of page\nADD appends link to section\nDEL deleats link\nDELSEC deleats the targeted section header\nHELP prints help")
    sys.exit()
if len(sys.argv) == 3:
    file = sys.argv[2]
    if isfile(file) == False:
        print(file + " NOT FOUND\ndefalting to /home/user/.config/homepage.html")
        file = "/home/user/.config/homepage.html"
else:
    file = "/home/user/.config/homepage.html"

if state == "APPEND" or state == "ADD":
    print("title")
    title = input()
    if state == "ADD":
        print("addr")
        addr = input()
# state
# 0 appends a section to the page
# 1 appends a link to the end of the selected section
# 2 edit mode? lets you remove bookmarks by section 

targetFile = open(file,"r")
targetText = targetFile.readlines()
targetFile.close()



def appendLink(title,addr):
    return "    <p>"+title+"\n      <a href='"+addr+"'>"+addr+"</a></p>\n"
def appendSection(title):
    return "<h1>"+title+"</h1>\n"

sectionList = []
sectionListLine = []
for i in range(1,len(targetText)):
    line = targetText[i]
    if line[0]+line[1]+line[2]+line[3] == "<h1>":
        line = line.replace("</h1>\n","")
        line = line.replace("<h1>","")
        sectionList.append(line)
        sectionListLine.append(i)

#sets target section
if state != "APPEND":
    sectionReturnString = ""
    for i in range(0,len(sectionList)):
        sectionReturnString = sectionReturnString + sectionList[i] + " - " + str(i) + "\n"
    print(sectionReturnString)
    targetSection = int(input())
else:
    targetText.insert(len(targetText)-2,appendSection(title))
    print(appendSection(title))
if state == "ADD":
    if targetSection>= len(sectionListLine)-1:
        targetText.insert(len(targetText)-2,appendLink(title,addr))
    else:
        targetText.insert(sectionListLine[targetSection+1],appendLink(title,addr))
    print(appendLink(title,addr))

#link remover
elif state == "DEL":
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
elif state == "DELSEC":
    del targetText[sectionListLine[targetSection]]
targetFile = open("/home/user/.config/homepage.html","w")
for text in targetText:
    targetFile.write(text)
  
