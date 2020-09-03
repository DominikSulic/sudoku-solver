import Solving_algorithm
import InputBox
import pygame
import numpy
from tkinter import *
from tkinter import messagebox


sudokuGrid = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,0,0]] 

"""
sudokuGrid = [[0,0,0,6,0,2,8,0,4],
            [0,0,0,0,3,0,0,0,7],
            [0,0,0,0,0,0,0,0,0],
            [4,0,6,0,5,0,3,0,0],
            [2,0,8,0,0,0,0,0,0],
            [0,0,0,0,0,0,9,1,0],
            [1,0,0,0,0,0,2,0,0],
            [0,7,0,9,0,0,0,5,0],
            [0,0,2,4,0,0,0,0,8]] """

pygame.init()
inputBoxes = []
clickableButtons = []
solver = Solving_algorithm.Solver()
allPosibleSolutions = solver.getSolutions(sudokuGrid) # Can sometimes take long if the puzzle is difficult but whatever
#print(allPosibleSolutions)
displayMessage = ''
if len(allPosibleSolutions) == 1:
    displayMessage = 'Correct! That is the only possible solution.'
else:
    displayMessage = 'Correct! In total, there are ' + str((len(allPosibleSolutions))) + ' possible solutions.'

# Screen things
WIDTH = 600
HEIGHT = 700
SUDOKU_WIDTH = 540
ROWS = 9
spacing = round(SUDOKU_WIDTH / ROWS, 2)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


def drawGrid():
    window.fill((255,255,255))

    startingX = (WIDTH - SUDOKU_WIDTH) / 2
    x = startingX
    y = startingX
    lineThickness = 1

    for i in range(10):
        if i % 3 == 0: 
            lineThickness = 4
        else:
            lineThickness = 1
        pygame.draw.line(window, (0,0,0), (startingX, x), (WIDTH - startingX, x), lineThickness)
        pygame.draw.line(window, (0,0,0), (x, startingX), (x, WIDTH - startingX), lineThickness)
        y += spacing
        x += spacing

    displayNumbers()
    displayButton()
    pygame.display.update()


def displayButton():
    clickableButtons.append(InputBox.InputBox(400, 600, 90, 30, 'Check'))
    clickableButtons[0].drawClickableButtons(window)


def displayNumbers():
    startingX = (WIDTH - SUDOKU_WIDTH) / 2
    x = startingX
    y = startingX
    number = 1

    for i in range(1, 82):
        Box = InputBox.InputBox(x, y, spacing, spacing)
        inputBoxes.append(Box)
        if i % 9 == 0:
            x = startingX
            y = startingX + spacing * number
            number += 1
        else:
            x += spacing

    counter = 0

    for row in range(9):
        for column in range(9):
            if sudokuGrid[row][column] != 0:
                inputBoxes[counter].drawGivenNumbers(window, str(sudokuGrid[row][column]))
            counter += 1


def markWrongCheckSimilarSolution(userSolution):
    # The function marks the wrong answers according to the correct solution that is the most similar
    # This is just some random way of marking wrong solutions, as if there are 4 correct solutions, it gets weird
    # so i'll just go by the number of wrong answers...

    listOfWrongAnswers = []
    wrongAnswers = 0

    for solution in allPosibleSolutions:
        for row in range(9):
            for column in range(9):
                if userSolution[row][column] != solution[row][column]:
                    wrongAnswers += 1
        listOfWrongAnswers.append(wrongAnswers)
        wrongAnswers = 0
    
    smallestNumberOfMistakes = 81

    for i in range(len(listOfWrongAnswers)):
        if listOfWrongAnswers[i] < smallestNumberOfMistakes:
            smallestNumberOfMistakes = listOfWrongAnswers[i]

    indexOfTheChosenSolution = 0

    for i in range(len(listOfWrongAnswers)):
        if smallestNumberOfMistakes == listOfWrongAnswers[i]:
            indexOfTheChosenSolution = i
    
    counter = 0
    for row in range(9):
        for column in range(9):
            if inputBoxes[counter].text == '':
                inputBoxes[counter].markWrong(True)
            else:
                if allPosibleSolutions[indexOfTheChosenSolution][row][column] != int(inputBoxes[counter].text):
                    inputBoxes[counter].markWrong(True)
                else:
                    inputBoxes[counter].markWrong(False)
            counter += 1
        

def compareSolutions():
    # Compares the user solution to the actual solution(s)
    userSolution = numpy.zeros((9,9), int)
    counter = 0

    for row in range(9):
        for column in range(9):
            if inputBoxes[counter].text == '':
                userSolution[row][column] = 0
            else:
                userSolution[row][column] = int(inputBoxes[counter].text)
            counter += 1
        
    markWrongCheckSimilarSolution(userSolution)

    for solution in allPosibleSolutions:
        # Uses numpy comparison for the whole array
        if (solution == userSolution).all():
            Tk().wm_withdraw()
            messagebox.showinfo('', displayMessage)
    



def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            for box in inputBoxes:
                box.handleEvent(event)
            for box in inputBoxes:
                box.drawUserNumbers(window)
            if clickableButtons[0].buttonClicked(event):
                compareSolutions()

        pygame.display.update()


if __name__ == '__main__':
    drawGrid()
    main()
    pygame.quit()