'''
    Problem Link:-https://www.hackerrank.com/challenges/plus-minus/problem
'''

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero, negative, positive = 0, 0, 0
    length = len(arr)
    for element in arr:
        if element == 0:
            zero += 1
        elif element < 0:
            negative += 1
        elif element > 0:
            positive += 1

    print("{:.6f}\n{:.6f}\n{:.6f}\n".format(positive/length, negative/length, zero/length))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

