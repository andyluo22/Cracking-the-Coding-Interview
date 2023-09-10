# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
# column are set to 0

from typing import List
import unittest
from copy import deepcopy

def zero_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    
    row_set = set()
    col_set = set()
    
    for m in range(rows):
        for n in range(cols):
            if matrix[m][n] == 0:
                row_set.add(m)
                col_set.add(n)
    
    for m in range(rows):
        for n in range(cols):
            if matrix[m][n] != 0: # don't really need this constant time check
                if (m in row_set) or (n in col_set):
                    matrix[m][n] = 0 
    
    return matrix

                
class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [zero_matrix]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()