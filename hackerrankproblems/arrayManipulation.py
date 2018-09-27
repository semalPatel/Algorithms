#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    maxValue = 0
    x = 0
    initialArray = [0]*(n+1);
    for i in queries:
        firstIndex = i[0]-1
        secondIndex = i[1]-1
        initialArray[firstIndex] += i[2]
        initialArray[secondIndex+1] -= i[2]
    for i in range(len(initialArray)):
        x = x+initialArray[i]
        if maxValue < x:
            maxValue = x
    return maxValue

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
