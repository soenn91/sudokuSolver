# -*- coding: utf-8 -*-
"""
Back tracking algorithm for solving a sudoku

@author: Adrian Anton
"""
import numpy as np

def FindEmpty(sudoku, coords):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                coords[0]=i
                coords[1]=j
                return True
    # All filled, it is done        
    return False
         

def CheckRow(sudoku,x,number):
    for i in range(9):
        if sudoku[x][i] == number:
            return True        
    return False
 
       
def CheckCol(sudoku,y,number):
    for i in range(9):
        if sudoku[i][y] == number:
            return True        
    return False
  

def CheckCell(sudoku,x,y,number):
    for i in range(3):
        for j in range(3):
            if sudoku[i+x][j+y] == number:
                return True
    return False
                
   
def SafeAss(sudoku, x,y,number):
    # if check functs return False means it is safe and return True
    return not CheckRow(sudoku,x,number) and not CheckCol(sudoku,y,number) and not CheckCell(sudoku,x - x%3,y - y%3,number)
  
def RecurSolve(sudoku):
    cord = np.zeros(2).astype(np.uint8)
    if (not FindEmpty(sudoku, cord)):
        # COMPLETE
        return True
    row = cord[0]
    col = cord[1]
    for digit in range(1,10):
        #print "Digit: "
        #print digit
        if (SafeAss(sudoku, row, col, digit)):
            sudoku[row][col] = digit
            if (RecurSolve(sudoku)):
                return True
            # set to 0 to try with the next digit
            sudoku[row][col] = 0            
    return False
          
if __name__ == "__main__": 
     
    randomSudoku = np.array([[5,3,0,0,7,0,0,0,0],
                             [6,0,0,1,9,5,0,0,0],
                             [0,9,8,0,0,0,0,6,0],
                             [8,0,0,0,6,0,0,0,3],
                             [4,0,0,8,0,3,0,0,1],
                             [7,0,0,0,2,0,0,0,6],
                             [0,6,0,0,0,0,2,8,0],
                             [0,0,0,4,1,9,0,0,5],
                             [0,0,0,0,8,0,0,7,9]])    
    if RecurSolve(randomSudoku):
        print "Done"
    else:
        print "No solution exists"