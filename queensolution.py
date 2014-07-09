#-------------------------------------------------------------------------------
# Name:        queensolution
# Purpose:
#
# Author:      Rodolfo
#
# Created:     06/11/2012
# Copyright:   (c) Rodolfo 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

class QueenSolution:
    def __init__(self, no_of_queens = 8):
        self.noqueens = no_of_queens
        self.queens = []
        for i in range(no_of_queens):
            self.queens.append(0)

    def addQueen(self, x, y):
        self.queens[x - 1] = y

    def getQueen(self, x):
        return self.queens[x - 1]

    def getQueenAlgebraix(self, x):
        y = 0
        y = self.queens[x - 1]
        i_x = ord('a') + x - 1
        c_x = chr(i_x)
        return c_x + ' ' + chr(ord('0') + y )

    def getAllAlgebraic(self):
        solutions = []
        for i in range(1, self.noqueens + 1):
            solutions.append(self.getQueenAlgebraix(i))
        return solutions






if __name__ == '__main__':
    main()
