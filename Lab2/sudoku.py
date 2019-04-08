# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:43:10 2019

@author: Minh Ta
"""
import numpy as np

def convertToGrid(numberString):
    """ converts the 81-digit numberString into a 9x9 numpy array """
    numList = [int(ch) for ch in numberString]
    numArr = np.reshape(np.array(numList),(9, 9))
    return numArr

correctSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
def correctSudoku(sudoku):
    """ returns true if the sudoku grid is correct """
    
    """ rows col """
    for i in range (0, 9):
    	rowFalse = set(np.reshape(sudoku[i, :], (9))) != correctSet
    	colFalse = set(np.reshape(sudoku[:, i], (9))) != correctSet
        if rowFalse or colFalse:
            return False
    
    """ 3x3 """
    for i in range(0, 3):
        for j in range(0, 3):
            threeTimesThree = sudoku[i * 3:(i + 1) * 3, j * 3:(j + 1)*3]
            if set(np.reshape(threeTimesThree, (9))) != correctSet:
                return False
    return True

with open('sudoku_solutions.txt', 'r') as inputFile:
    lines = [str.split(line.rstrip(), ": ")[1] for line in inputFile]

for i in range(len(lines)):
    if correctSudoku(convertToGrid(lines[i])):
        print(str(i) + " correct")
    else:
        print(str(i) + " incorrect")
