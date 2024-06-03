import numpy as np
import sys

class Sudoku:
    def __init__(self, array=None):
        if array is None:
            self.entries = np.zeros((9, 9), dtype=int)
            self.Create_Sudoku_Manually()
        else:
            self.entries = array
        # Erstelle ein Array mit den Zahlen 1 bis 9
        true_array = np.ones(9, dtype=bool)
        # Wiederhole dieses Array für jedes Feld im 9x9-Grid
        self.pos_entries = np.tile(true_array, (9, 9, 1))
        
    def get_Entries(self) -> np.ndarray:
        return self.entries

    def get_Pos_Entries(self) -> np.ndarray:
        return self.pos_entries
    
    def set_Pos_Entries(self, pos_entries):
        self.pos_entries = pos_entries
        
    def get_Entries(self) -> np.ndarray:
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

    def Create_Sudoku_Read(self, array):
        print()
        
        
class Sudoku_Helper:

    def Print(sudoku):
        entries = sudoku.get_Entries()
        frame_length = 3*9 + 2 + 6
        
        print("Sudoku: ")
        for row in range (entries.shape[0]):
            if(row == 0 or row == 3 or row == 6):
                for i in range(3*9 + 4 + 6):
                    sys.stdout.write("-")
                print()
            for col in range (entries.shape[1]):  
                if(col == (0)):
                    sys.stdout.write("| ")
                if(entries[row][col] == 0):
                    sys.stdout.write("   ")
                else:
                    sys.stdout.write(" " + str(entries[row][col]) + " ")
                if(col == 2 or col == 5): 
                    sys.stdout.write(" | ")
                elif(col == (8)):
                    sys.stdout.write(" |")
                    
            print()
        for i in range(frame_length +2 ):
            sys.stdout.write("-")
        print()
    
    def Print_Pos_Entries(sudoku, row, col):
        print(sudoku.get_Pos_Entries()[row][col])    
            
class Sudoku_Solver:
    def Get_Row_Col(sudoku, row, col) -> np.ndarray:
        entries = sudoku.get_Entries()
        neighbours = np.zeros((9), dtype= bool)
        #check column
        for i in range(9):
            if(i != col):
                current = entries[row][i]
                if(current != 0):
                    neighbours[current -1] = True
        for i in range(9):
            if(i != row):
                current = entries[i][col]
                if(current != 0):
                    neighbours[current -1] = True
        #print(neighbours)
        return neighbours
                
    def Get_Block(sudoku, row, col) -> np.ndarray:
        entries = sudoku.get_Entries()
        neighbours = np.zeros((9), dtype= bool)
        block_row = row // 3 
        block_col = col // 3
        
        for i in range(block_row * 3, block_row * 3 + 3):
            for j in range(block_col * 3, block_col * 3 + 3):
                current = entries[i][j]
                if(current != 0):
                    neighbours[current -1] = True
        #print(neighbours)
        return neighbours
    
    def Update_Possible_Entries(sudoku, neighbours, col, row):
        pos_entries = sudoku.get_Pos_Entries()
        for i in range(0,9):
            if(neighbours[i]):
                pos_entries[row][col][i] = False
        print("row: ", row,  "col: ", col,  "pos_entries: ", pos_entries[row][col])
        sudoku.set_Pos_Entries(pos_entries)
    
    #checks for all entries the box and row and line neighbours
    def Update_Box_RowCol(sudoku):
        for i in range(0,9):
            for j in range(0,9):
                neighbours = Sudoku_Solver.Get_Block(sudoku, i,j) | Sudoku_Solver.Get_Row_Col(sudoku, i, j)
                Sudoku_Solver.Update_Possible_Entries(sudoku, neighbours,i,j)
                print("row: ", i,  "col: ", j,  "neighbours: ", neighbours)
                

