#!/bin/python
import random,sys
random.seed()

#commands are ./main.py AI_AMOUNT PLAYERS PLAYERS
# ./ main.py 2 bill bob
# will make 2 players and 2 ais
# lets you add more players with the command line 
print(len(sys.argv))
if len(sys.argv) >= 2:
    playerName = []
    ainumber = int(sys.argv[1])
    for i in range(len(sys.argv)-2):
        playerName.append(sys.argv[i+2])
else:
    playerName = ["Bryce"]
    ainumber = 1

playerClasses = []
class player:
    def __init__(self,name):
        self.score = 0
        self.name = name
    def play(self):
        add = 0
        loops = 0
        loop = True
        while loop == True:
            loops = loops + 1
            rolled = random.randint(1,6) 
            if rolled == 1:
                add = 0
                print(self.name +"rolled 0")
                loop = False
                
            else:
                add = add + rolled
                loop = self.choice(rolled,add,loops)
        self.score = add + self.score
        if self.score >= 100:
            print(self.name +" has won")
            return True
        else:
            return False
    def choice(self,rolled,add,loops):
        print(self.name+" rolled " + str(rolled) +" for a score of " + str(add) + " loops "+str(loops)+" play more?")
        userResponse = input()
        if userResponse != "y":
            return False
        else:
            return True
    def printscore(self):
        print(self.name + " " + str(self.score))
class ai(player):
    def choice(self,rolled,add,loops):
        goOn = random.random()
        print(self.name + " rolled " + str(rolled) + " score " + str(add) + "loops" + str(loops))
        if goOn <= .04*loops**2:
            return True
        else:
            return False

#makes playable players
for i in range(len(playerName)):
    playerClasses.append(player(playerName[i]))

#makes ai players
if ainumber != 0:
    for i in range(0,ainumber):
        playerClasses.append(ai("ai"+str(i)))
playerInt = 0

while True:
    if True == playerClasses[playerInt].play():
        break
    playerClasses[playerInt].printscore()
    playerInt = playerInt + 1
    if playerInt > len(playerClasses)-1:
        playerInt = 0
