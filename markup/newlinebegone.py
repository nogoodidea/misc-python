#!/bin/python
#new line be gone
def nlbg(input):
    input = input.replace("\n","")
    return input.strip()
    
#self test for nlbg
if __name__ == "__main__":
    testtext = "i\n hate\n newlines"
    print(nlbg(testtext))
    
