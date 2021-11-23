#!/bin/python
import sys,cgi,fnmatch

targetFile = open("/home/user/.config/homepage.html","r")
targetText = targetFile.readlines()
targetFile.close()
form = cgi.FildStorage()
if "title" not in form or "state" not in form:
    print("<title>ERROR</title>")
    sys.exit()

#gets vaule from cgi
title = form.getfirst("user", "")
addr = form.getfirst("addr", "")
state = form.getfirst("state", "")
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
    targetText.insert(len(targetText)-2,appendSection(title))
elif state == 2:
    targetText.insert(len(targetText)-2,appendLink(title,addr))

targetFile = open(".config/homepage.html","w")
for text in targetText:
    targetFile.write(text)
    
