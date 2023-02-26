#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    dic={}
    for i in range(len(s)):
        if(s[i]!=" "):
            dic[s[i]]= 0
    
    # Write your code here
    if(len(dic)==26):
        print("pangram")
    else:
        print("not pangram")

if __name__ == '__main__':


    s = input().upper()
    result = pangrams(s)
