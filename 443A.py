'''
https://codeforces.com/problemset/problem/443/A
Author: Arrow
'''
inputString = input()

splitString = list(inputString)

if(len(splitString)==2):
    print(0)
else:
    splitString = splitString[1::3]
    splitString = set(splitString)
    print(len(splitString))
