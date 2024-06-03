from Sudoku import Sudoku
from Sudoku import Sudoku_Helper
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