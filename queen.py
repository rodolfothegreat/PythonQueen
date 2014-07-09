#-------------------------------------------------------------------------------
# Name:        queen
# Purpose:
#
# Author:      Rodolfo d'Ettorre
#
# Created:     24/10/2012
# Copyright:   (c) Rodolfo 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import queensolution
import string

class Vector:
    def __init__(self, ax = 0, ay = 0):
        self.x = ax
        self.y = ay


class Queen:
    def __init__(self, nofqueens = 8):
        self.nofqueens = int(nofqueens)
        self.queenlst = []
        for i in range(nofqueens):
            self.queenlst.append(Vector(i + 1, 0))
        self.solutionList = []
        self.counter = 0

    def getCountSolutions(self):
        return len(self.solutionList)

    def getOneSolution(self, anIndex):
        if self.solutionList.count > 0:
            return self.solutionList[anIndex]
        else:
            return None

    def findOneSolution(self):
        for i in range(self.nofqueens):
            avector = self.queenlst[i]
            avector.y = 0
        self.counter = 0
        self.solutionList = []
        self.moveQueen(0)

    def isVacant(self, x, y):
        if x == 0:
            return True
        iRow = x
        for i in range(iRow):
            aVector = self.queenlst[i]
            if y == aVector.y:
                return False
            if abs(y - aVector.y) == abs(x - aVector.x):
                return False

        return True


    def moveQueen(self, anIndex = 0):
        aNewCol = 0
        if anIndex > self.nofqueens - 1:
            self.counter += 1
            #print "Solution %d \n" % self.counter
            aqueenie = queensolution.QueenSolution(self.nofqueens)
            for i in range(self.nofqueens):
                avector = self.queenlst[i]
                #print "%d - %d \n" %(avector.x, avector.y)
                aqueenie.addQueen(avector.x, avector.y)
            self.solutionList.append(aqueenie)
            #print("--------------------------------------- \n");
            return -1

        for i in range (1, self.nofqueens + 1):
            if self.isVacant(anIndex + 1, i):
                avector = self.queenlst[anIndex]
                avector.y = i
                if (self.moveQueen(anIndex + 1) == -1):
                    continue
                aNewCol = i
                break

        if (aNewCol == 0):
            for i in range(anIndex, self.nofqueens):
                avector = self.queenlst[i]
                avector.y = 0
            return -1
      
        return 0





def main():
    findQueen = Queen(8)
    print("Start \n")
    findQueen.findOneSolution()
    print "There are " + repr(findQueen.getCountSolutions()) +  " solutions\n" 
    for i in range(0, findQueen.getCountSolutions() - 1):
      asolution = findQueen.solutionList[i]
      print asolution.getAllAlgebraic()
    #print asolution
    input("\npress any key\n")
if __name__ == '__main__':
    main()
