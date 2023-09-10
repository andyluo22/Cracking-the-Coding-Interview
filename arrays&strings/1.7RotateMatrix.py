# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

from typing import List

# Tips: Keep track of each layer (a layer is defined as a ring)
# For each layer, from the first to last index (exclusing the end) we perform the same algorithm
def rotate_matrix(matrix):
    """rotates a matrix 90 degrees clockwise"""
    n = len(matrix)
    num_layers = n // 2
    for layer in range(num_layers):
        first, last = layer, n - layer - 1
        for i in range(first, last):

            top = matrix[layer][i]

            matrix[layer][i] = matrix[n - i - 1][layer]

            matrix[n - i - 1][layer] = matrix[n - layer - 1][n - i - 1]

            matrix[n - layer - 1][n - i - 1] = matrix[i][n - layer - 1]

            matrix[i][n - layer - 1] = top

            # matrix[layer][i] = top
            # matrix[n - i - 1][layer] = left
            # matrix[n - layer - 1][n - i - 1] = bottom
            # matrix[i][n - layer - 1] = right

    return matrix


threebythree = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

fourbyfour = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

fivebyfive = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]


rotated_matrix_three = rotate_matrix(threebythree)

rotated_matrix_four = rotate_matrix(fourbyfour)

rotated_matrix_five = rotate_matrix(fivebyfive)

print(rotated_matrix_five)

import unittest
from copy import deepcopy

class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        rotate_matrix,
    ]

    def test_rotate_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected

if __name__ == "__main__":
    unittest.main()