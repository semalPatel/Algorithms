import math
import os
import random
import re
import sys
import collections


def get_rth_element(matrix, min_bound, max_bound, R):
    r = max_bound[0] - min_bound[0]
    c = max_bound[1] - min_bound[1]
    if R < r:
        Br = min_bound[0]
        x = Br + R
        y = min_bound[0]
    elif R < r + c:
        Bc = min_bound[0]
        x = max_bound[0]
        y = Bc + R - r
    elif R < 2 * r + c:
        Br = max_bound[0]
        x = Br - R + r + c
        y = max_bound[1]
    else:
        Bc = max_bound[1]
        x = min_bound[0]
        y = Bc - R + 2 * r + c
    return [x, y]

def matrixRotation(matrix, r):
    m = len(matrix) - 1
    n = len(matrix[-1]) - 1
    slices = min(m, n)//2 + 1
    print(m, n, slices)
    copy_r = r
    for x in range(slices):
        total = 2*(m - x*2) + 2*(n - x*2)
        r = r % total
        buffer = []
        for y in range(total):
            current = get_rth_element(matrix, [x, x], [m - x, n - x], y)
            buffer.append(matrix[current[0]][current[1]])
        for y in range(total):
            rth = get_rth_element(matrix, [x, x], [m - x, n - x], (y + r) % total)
            matrix[rth[0]][rth[1]] = buffer[y]
    r = copy_r

    for row in matrix:
        print(' '.join(map(str,row)))

matrix = [
        [1 , 2 , 3 , 4 , 2, 3],
        [5 , 6 , 7 , 8 , 6, 1],
        [9 , 10, 11, 12, 9, 5],
        [3 , 14, 15, 16, 1, 7],
        [3 , 14, 15, 16, 3, 0],
        [14, 14, 15, 16, 5, 4],
        [3 , 14, 15, 16, 0, 6],
        [7 , 18, 19, 20, 4, 8]
    ]
matrixRotation(matrix, 42971434)
