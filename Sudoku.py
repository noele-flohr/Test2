import numpy as np

class Sudoku:
    def __init__(self):
        self.entries = np.zeros((9,9), dtype = int)
        self.Create_Sudoku_Manually()
    
    def get_entries(self) -> np.array:
        return self.entries
    
    def Create_Sudoku_Manually(self):
        for row in range (self.entries.shape[0]):
            for col in range (self.entries.shape[1]):                    
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

class Sudoku_Helper:
    def Get_Row_Col(self, sudoku, row, col) -> np.array:
        entries = sudoku.get_entries()
        neighbours = np.zeros((9), dtype= bool)
        #check column
        for i in range(9):
            if(i != col):
                current = sudoku.entries[row][i]
                if(current != 0):
                    neighbours[current -1] = True
        for i in range(9):
            if(i != row):
                current = sudoku.entries[i][col]
                if(current != 0):
                    neighbours[current -1] = True
        return neighbours
                
    #def Get_Block(self, sudoku, row, col):
                
    def Print(self, sudoku):
        print("")
            

class SolvingSudoku:
    def __init__():
        sudoku = Sudoku()

