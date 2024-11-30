# Sudoku Solver

Here you will find a Python script I wrote in my free time to solve any Sudoku grid using a brute-force strategy.

## Running the script

To run the script, make sure you have the NumPy library installed.

```
pip3 install numpy
```

Then run the script using your version of Python, for instance:

```
python3.10 sudoku_solver.py
```
## User Input

When prompted for user input, enter your Sudoku grid as an 81-digit-long string, using 0 for blanks.
The backtracking algorithm used computes every possible solution one by one and asks for user input to continue after each solution found.
Type "n" to stop, and any other input to continue.

## Algorithm

The algorithm implements a brute-force "try all possible solutions one by one" backtracking strategy.
A backtracking algorithm recursively explores all possible solutions. Solutions are tried one by one and the program undoes them, or "backtracks", if it hits a dead end.

The time complexity is O(9**n) where n is the number of blanks (zeroes) in the starting grid.
The general problem of solving a Sudoku grid is known to be NP-complete. An exponential-time complexity means that, for a large enough n coupled with a difficult unique-solution puzzle, finishing the computation could require more time than the age of universe.
