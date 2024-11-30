import numpy as np
import re

hasASolution = False

string = input("Enter grid (return for default):")

#Default grid
grid = [[3,6,0,0,0,7,0,0,2],
        [0,0,0,8,0,0,0,7,6],
        [0,0,0,0,5,0,1,4,0],
        [0,3,0,7,0,0,9,0,0],
        [9,7,2,0,0,0,5,8,3],
        [0,0,1,0,0,5,0,2,0],
        [0,1,8,0,3,0,0,0,0],
        [6,4,0,0,0,8,0,0,0],
        [2,0,0,1,0,0,0,9,8]]

if string != "":
    #Parse user-input grid string
    regex = re.compile("[0-9]")
    for x in range(9):
        for y in range(9):
            match = regex.search(string)
            if match is None:
                print("Invalid input grid!")
                print("Please enter a valid 81-digit (9x9) string")
                print("Use 0's for blanks")
                print("The string must read each row one by one left to right")
                print("starting with the top row and going down")
                exit()
            grid[x][y] = int(match.group())
            string = string[match.end():]

def box_digits(x, y):
    '''Returns the list of 9 digits in the box of grid[x][y].'''
    #Find left-corner box digit
    x_ = x - (x % 3)
    y_ = y - (y % 3)
    digits = [grid[x_ + dx][y_ + dy] for dx in range(3) for dy in range(3)]
    return digits

def isPossible(d, x, y):
    '''Returns True if digit d (1-9) is possible to write in grid[x][y].
       False otherwise.'''
    #Check if d is in the row
    if d in grid[x]:
        return False
    #Check if d is in the column
    if d in [grid[i][y] for i in range(9)]:
        return False
    #Check if d is in the box
    if d in box_digits(x, y):
        return False
    return True

def backtrack_solve():
    '''Solve soduko grid'''
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for d in range(1,10):
                    if isPossible(d, x, y):
                        grid[x][y] = d
                        backtrack_solve()
                        grid[x][y] = 0
                return
    hasASolution = True
    print(np.array(grid))
    #Prompt user input for computing the next solution (if multiple solutions)
    findMoreSolutions = input("Find more solutions (y/n)? ")
    if findMoreSolutions ==  "n":
        exit()

#Check input grid is valid
for x in range(9):
    for y in range(9):
        if grid[x][y] != 0:
            d = grid[x][y]
            grid[x][y] = 0
            if not isPossible(d, x, y):
                print("The grid entered is not a valid Sudoku grid")
                print("The starting grid must not have row, column, or box conflicts")
                exit()
            grid[x][y] = d

#Solve puzzle
backtrack_solve()
if not hasASolution:
    "The Sudoku grid has no solution"
