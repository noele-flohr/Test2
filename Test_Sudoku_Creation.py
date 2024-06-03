from Sudoku import Sudoku
from Sudoku import Sudoku_Helper
from Sudoku import Sudoku_Solver
import numpy as np

sudoku = np.array([[0,7,0,5,8,3,0,2,0],
          [0,5,9,2,0,0,3,0,0],
          [3,4,0,0,0,6,5,0,7],
          [7,9,5,0,0,0,6,3,2],
          [0,0,3,6,9,7,1,0,0],
          [6,8,0,0,0,2,7,0,0],
          [9,1,4,8,3,5,0,7,6],
          [0,3,0,7,0,1,4,9,5],
          [5,6,7,4,2,9,0,1,3]
          ])

test_sudoku = Sudoku(sudoku)

Sudoku_Helper.Print(test_sudoku)
#entries =test_sudoku.get_Pos_Entries()
block_neigbours = Sudoku_Solver.Get_Block(test_sudoku, 0, 0)
rowcol_neighbours = Sudoku_Solver.Get_Row_Col(test_sudoku, 0, 0)
common_neighbours = block_neigbours | rowcol_neighbours
print(common_neighbours)
#Sudoku_Solver.Update_Possible_Entries(test_sudoku, block_neigbours, 0, 0)
#Sudoku_Solver.Update_Possible_Entries(test_sudoku, rowcol_neighbours, 0, 0)
#Sudoku_Solver.Print_Pos_Entries(test_sudoku, 0, 0)
Sudoku_Solver.Update_Box_RowCol(test_sudoku)