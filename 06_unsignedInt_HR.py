#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    n=bin(n)
    n=str(n)
    n=n[2::]
    bits = ""
    def replace(s,i):
        temp = list(n)
        temp[i] = s
        return "".join(temp)

    for i in range(len(n)):
        if(n[i]=='0'):
            n= replace("1", i)
        else:
            n= replace("0", i)

    result=0
    for _ in range(32-len(n)):
        bits=bits+"1"
    
    bits=bits+n

    for i in range(len(bits)):
        result=(int(bits[i])*(2**(31-i)))+result
    
    print(result)

    # Write your code here



if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
