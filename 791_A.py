'''
https://codeforces.com/problemset/problem/791/A
Author: Arrow
'''
def getResult(a,b,result):
    a = a*3
    b = b*2
    result = result+1
    if(a>b):
        return result
    
    return getResult(a,b,result)


a , b = map ( int, input().split())
print(getResult(a,b,0))
