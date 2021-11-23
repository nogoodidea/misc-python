#!/bin/python
import sys,fnmatch

targetFile = open("/home/user/.config/homepage.html","r")
targetText = targetFile.readlines()
targetFile.close()

# handles seting state, defalt state is 1
if len(sys.argv) <= 1:
    state = int(sys.argv[1])
else:
    state = 2
if state == 1 or state == 2:
    print("title\n>")
    title = input()
if state == 2:
    print("addr\n>")
    addr = input()
# state
# 0 returns a list of sections
# 1 appends a section to the page
# 2 appends a link to the end of the page

def appendLink(title,addr):
    return "<p>"+title+"\n<a href='"+addr+"'>"+addr+"</a></p>"
def appendSection(title):
    return "<h1>"+title+"</h1>"


sectionList = []
if state == 0:
    for text in targetText:
        if fnmatch.filter(text,"<h1>*</h1>") != "":
            text = text.replace("<h1>")
            text = text.replace("</h1>")
            sectionList.append(text)
    print("<p>")
    print(sectionList)
    print("</p>")
elif state == 1:
    targetText.insert(len(targetText)-3,appendSection(title))
    print(appendSection(title))
elif state == 2:
    targetText.insert(len(targetText)-3,appendLink(title,addr))
    print(appendLink(title,addr))

targetFile = open("/home/user/.config/homepage.html","w")
for text in targetText:
    targetFile.write(text)
    
