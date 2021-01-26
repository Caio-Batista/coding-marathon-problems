
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    right_sum = 0
    left_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==j:
                left_sum += arr[i][j]
                right_sum += arr[i][len(arr) - 1 - j]
    return abs(right_sum - left_sum)

if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)
    print(result)