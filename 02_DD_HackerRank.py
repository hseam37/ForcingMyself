#!/bin/python3

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
    # Write your code here
    if(len(arr)==1):
        return 0
    
    a=b=0
    i=0
    j=k=len(arr)-1

    xDiagonal=yDiagonal=0

    while(i<=k):
        xDiagonal+=arr[a][b]
        yDiagonal+=arr[i][j]
        a+=1
        b+=1
        i+=1
        j-=1

    return abs(xDiagonal-yDiagonal)



if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
