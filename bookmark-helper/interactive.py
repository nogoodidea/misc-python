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
# 1 appends a link to the end of the selected header
# 2 lists all headers TODO
## RETURNS DO NOT WORK WITH HTML PARSER CLASS


def appendLink(title,addr):
    return "    <p>"+title+"\n  <a href='"+addr+"'>"+addr+"</a></p>\n"
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

if state == 0:
    targetText.insert(len(targetText)-2,appendSection(title))
    print(appendSection(title))
elif state == 1:
    sectionReturnString = ""
    for i in range(0,len(sectionList)):
        sectionReturnString = sectionReturnString + sectionList[i] + " - " + str(i) + " "
    print(sectionReturnString)
    input = int(input())
    print(len(sectionListLine))
    if input >= len(sectionListLine)-1:
        targetText.insert(len(targetText)-2,appendLink(title,addr))
    else:
        targetText.insert(sectionListLine[input+1],appendLink(title,addr))
    print(appendLink(title,addr))
     
targetFile = open("/home/user/.config/homepage.html","w")
for text in targetText:
    targetFile.write(text)
  
