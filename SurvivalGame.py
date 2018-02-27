#from Human import Human
#from Chark import Chark
from Player import Player
from Pos import Pos
#from Axe import Axe
from Obstacle import Obstacle
#from Rifle import Rifle
from Weapon import Weapon


class SurvivalGame(object):
    n = 0
    D = 10
    O = 2

    #   NOT SURE
    teleportObjects = [object() for x in range(10)]
    def __init__(self):
        print 'hi'

    def printBoard(self):
        printObject = [["  " for x in range(10)] for y in range(10)]
        i=0
        while(i<self.n):
            #???????????
            pos = Player(self.teleportObjects[i]).getPos()
            printObject[pos.getX()][pos.getY()] = Player(self.teleportObjects[i].getName())
            i += 1

        i=0
        while i<self.n :
            pos = Obstacle(self.teleportObjects[i]).getPos()
            printObject[pos.getX()][pos.getY()] = 'O' + i-self.n
            i += 1

        #print
        print " ",
        i=0
        while i<self.D:
            print("|  %d " % i),
            i += 1
        print("|")
        i=0
        while i < self.D*3.2 :
            print "-",
            i += 1
        print ""
        row=0
        while row < self.D:
            print row,
            col=0
            while col < self.D:
                print("| %s " %printObject[row][col]),
                col+=1
            print "|"
            i=0
            while i<self.D*3.2 :
                print "-",
                i+=1
            print ""
            row+=1

    def positionOccupied(self, randx, randy):
        for o in self.teleportObjects:
            if isinstance(o,Player):
                pos = Player(o).getPos()
                if pos.getX() == randx and pos.getY() ==randy :
                    return T


    def getPlayer(self, randx, randy):
        pass

    def init(self):
        pass

    def gameStart(self):
        pass


game = SurvivalGame()
game.printBoard()
#game.init()
#game.gameStart()
