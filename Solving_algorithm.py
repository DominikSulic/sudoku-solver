import math
import numpy

class Solver:
    def __init__(self):
        self.foundSolution = False

    def canPlaceNumber(self, sudokuGrid, row, column, number):
        for r in range(9):
            if(sudokuGrid[r][column] == number):
                return False

        for c in range(9):
            if(sudokuGrid[row][c] == number):
                return False

        sqrt = int(math.sqrt(len(sudokuGrid[0])))
        beginningRow = row - row % sqrt
        beginningColumn = column - column % sqrt

        for i in range(beginningRow, beginningRow+3):
            for n in range(beginningColumn, beginningColumn+3):
                if(sudokuGrid[i][n] == number):
                    return False
        
        return True

    def getSolutions(self, sudokuGrid):

        def solveUsingBacktracking(sudokuGrid):
            nonlocal solutions
            temp = numpy.zeros((9,9), int)

            for row in range(9):
                for column in range(9):
                    temp[row][column] = sudokuGrid[row][column]

            for row in range(9):
                for column in range(9):
                    if sudokuGrid[row][column] == 0:
                        for i in range(1,10):
                            if self.canPlaceNumber(sudokuGrid, row, column, i):
                                sudokuGrid[row][column] = i
                                temp[row][column] = i
                                solveUsingBacktracking(sudokuGrid)
                                sudokuGrid[row][column] = 0
                                temp[row][column] = 0
                        return
                    if row == 8 and column == 8 and sudokuGrid[row][column] != 0:
                        solutions.append(temp)

        solutions = []
        solveUsingBacktracking(sudokuGrid)
        # This part checks if the user put in the right numbers
        """ counter = 0
        incorrectlyPlacedNumbers = 0
        for solution in solutions:
            print("solution: ", solution)

        for x in range(9):
            for row in range(9):
                if counter >= 81:
                    counter = 0
                if inputBoxes[counter].givenNumber == False:
                    if inputBoxes[counter].text == '':
                        inputBoxes[counter].markWrong(True)
                        incorrectlyPlacedNumbers += 1
                    else:
                        if int(inputBoxes[counter].text) == sudokuGrid[x][row]:
                            inputBoxes[counter].markWrong(False)
                        else:
                            inputBoxes[counter].markWrong(True)
                            incorrectlyPlacedNumbers += 1
                counter += 1


        Tk().wm_withdraw()
        # displays both the messages
        if incorrectlyPlacedNumbers == 0:
            self.foundSolution = True

        if self.foundSolution == True:
            messagebox.showinfo('', 'Correct! (if there are squares marked red, they indicate that there are other possible solutions)')
        self.foundSolution = False """
        return solutions