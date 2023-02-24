#!/bin/python3

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    unique = 0
    for i in range(0,len(a)):
        flag=True
        for j in range(i+1,len(a)):
            if(a[i]==a[j]):
                a[i]=0
                a[j]=0
    a.sort()
    print(a[-1])

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)


