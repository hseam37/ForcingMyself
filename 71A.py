
'''
https://codeforces.com/problemset/problem/71/A
Author: Arrow
'''
testCase = int(input())

for i in range(testCase):
    inputString = list(input())
    strLength = len(inputString)
    if strLength<=10:
     print("".join(inputString))
    else:
     print("{}{}{}".format(inputString[0],strLength-2,inputString[strLength-1]))
