import numpy as np

class Sudoku:
    def __init__(self):
        entries = np.zeros(9,9)
        self.Create_Sudoku_Manually()
    
    def Create_Sudoku_Manually(self):
        for col, row in self.entries:
            valid_input = False
            while not valid_input:
                try:
                    value = int(input(f"Enter value for cell ({row+1}, {col+1}) [0 for empty]: "))
                    if 0 <= value <= 9:
                        self.entries[row, col] = value
                        valid_input = True
                    else:
                        print("Please enter a number between 0 and 9.")
                except ValueError:
                    print("Invalid input. Please enter an integer between 0 and 9.")

class SolvingSudoku:
    def __init__():
        sudoku = Sudoku()

