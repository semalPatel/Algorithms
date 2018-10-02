import math
import os
import random
import re
import sys
import collections

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    c1 = [0]*len(queries)
    for i in range(0, len(queries)):
        for j in range(0, len(strings)):
            if queries[i] == strings[j]:
                c1[i]+=1
    return c1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
