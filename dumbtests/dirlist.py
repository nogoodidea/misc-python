#!/bin/python
import os,sys
if len(sys.argv) > 0:
    target = sys.argv[1]
else:
     target=""
filelist = os.listdir(target)
print(filelist)

for file in filelist:
    print(os.path.isfile(file))
    if os.path.isfile(file) == True:
        print(str(file) + " is a file")
    else:
        print(str(file) + " is not a file")
    
