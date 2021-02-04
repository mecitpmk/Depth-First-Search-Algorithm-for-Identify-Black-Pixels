import numpy as np


class Pts:
    def __init__(self,R,C):
        self.R = R
        self.C = C

    def __repr__(self):
        return '({},{})'.format(self.R,self.C)

class DeepSearch:
    def __init__(self,maze):
        row,col = np.shape(maze)
        self.row = row-1
        self.column = col-1
        self.visitedArr = np.zeros((row,col)) #0 Not Visited  -> 1 is VisitedBefore.
        self.maze = maze
        self.combObjects = {} # {(6,11): [(6,12), (6,13), (7,13), (7,14), (7,15), (8,15), (8,14), (8,13)] -> 
                                #Key : Objects(Pointx,Pointy) Start points  and  Values : List ObjectLists[Ptx,Pty]

        self.runSoftware()
    
    def printStartPointsnValues(self):
        """
            In this function it will be show us to Start points and its nodes.
        """
        for pt in self.combObjects:
            print("*******************************")
            print("->Start Point is {}".format(pt))
            for nodes in self.combObjects[pt]:
                print("--->Node point is {}".format(nodes))
        print("*******************************")
    
    
    def runSoftware(self):
        """
            In this function Checks every Columns value of every rows. Scan the value of 1
            If the value 1 is identified check its before visited or not?
                    If its not visited before run the recursiveFunction to scan its nodes.
        """
        for r in range(self.row+1):
            for c in range(self.column+1):
                if self.checkisOne(r,c):
                    self.initialPts = Pts(r,c)
                    self.turnAround(r,c)
                    
    
    def turnAround(self,R,C,fromRecursive = False):
        """
            R  = int -> Row
            C = int -> Column
            fromRecursive = booelan -> Represent function call if its called from inside function
                                       Program will understand it and it will Create point according to that.

            Purposes: In this function first checks Row and Column value is not Exceed MATRIX SIZE,
                       If its not exceed, check its visited with self.checkisOne() function and after that
                        if -> the function called fromthe for loop in self.runSoftware function it means that 
                            Founded 1 in Current R,C values and initial point(Start Point) will be current R,C
                        else -> Start point allready exist current R,C values will be Node for the Start point.

        """
        if R > -1 and C > -1 and R <= self.row and C <= self.column:
            if self.checkisOne(R,C):
                if not fromRecursive:
                    self.combObjects[self.initialPts] = []
                else:
                    self.combObjects[self.initialPts].append(Pts(R,C))
                self.visitedArr[R][C] = 1
                self.maze[R][C] = 0
                self.turnAround(R,C+1,fromRecursive = True)
                self.turnAround(R+1,C,fromRecursive = True)
                self.turnAround(R+1,C-1,fromRecursive = True)
                self.turnAround(R-1,C+1,fromRecursive = True)
                self.turnAround(R-1,C,fromRecursive = True)
                self.turnAround(R,C-1,fromRecursive = True)
                self.turnAround(R+1,C+1,fromRecursive = True)
                self.turnAround(R-1,C-1,fromRecursive = True)


    def checkisOne(self,R,C):
        """
            Checks the given Row,Column Value is 1 and it not visited before.
            
            R  = int -> Row
            C = int -> Column
            Returns : boolean

        """
        if R > -1 and C > -1 and R <= self.row and C <= self.column:
            if self.maze[R][C] == 1 and self.visitedArr[R][C] == 0:
                return True
        return False

    def findRegions(self):
        """
            Returns Founded Region numbers.
        """
        return len(self.combObjects.keys())

    def findMaxRegVal(self):
        """
            Returns maximum Region value of combined 1
            Example :  1 1 1 0 0 1 1
                       1 1 1 0 0 0 0
            There is a two region , First region Combined value is 6
                                    Second region Combined value is 2
                                    So it should be return 6 in here.
        """
        l = [len(v) for v in self.combObjects.values()]
        return max(l)+1 # +1 because of the key. Don't forget it.
    
    def calculateMAXPercentage(self):
        """
            In this function calculates Percentage of how much percentage belongts to maximumBlackPixels
            Example lets say matrix dimension 15*15 it means that it has 225 pixels.
            So assume that we found maximum Black region as a 45(pixels) it will found ratio in given formula
            Percentage = maxValue*100/R*C
        """
        total = self.row*self.column
        maxFinded = float(self.findMaxRegVal()*100)
        return maxFinded/total
    
    def calculateRegionPerc(self):
        """
            This funtion calculates how much pixels belongs to the black as a percentage
            Assume that matrix dimension is 15*15 it means that it has 225 pixels.
            And assume that total regions(TOTAL BLACKS) is 80(pixels) and Python will found percentage in given formula
            Percentage = totalBlacks*100/R*C
        """
        total = self.row*self.column
        summation = self.findRegions()
        l = [len(v) for v in self.combObjects.values()]
        summation += sum(l)
        summation = float(summation*100)
        return summation/total
#####################################
arr = np.array([
            [0,0,0,0,0,1],
            [1,1,0,0,0,1],
            [1,1,1,0,0,0],
            [0,0,0,1,0,0]
            ])   ##Testing Purposes


otherArr = np.array([
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) # Testing Purposes nRegs should  be  =5 maxReg should be = 15

TESTOBJ = DeepSearch(otherArr)

TESTOBJ.printStartPointsnValues()
print("Founded Region Number is -> {}".format(
                                            TESTOBJ.findRegions())) # Show us regions

print("Max Value for the Black Pixels -> {}".format(TESTOBJ.findMaxRegVal())) # Show us maximum values.

print("HOW MUCH BLACK PIXELS COVERED IN THE ARRAY -> {}".format(
                                                        TESTOBJ.calculateRegionPerc()))


print("Finds MaxRegVal and calculate percentage how much of it belongs to maxRegVal -> {}".format(
                                                                                          TESTOBJ.calculateMAXPercentage()))

