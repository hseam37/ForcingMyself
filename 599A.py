'''
https://codeforces.com/problemset/problem/599/A
Author: Arrow
'''

d1,d2,d3  = map(int,input().split())

result = min(d1,d2)


if d1+d2 > d3:
    result = result + d3
else:
    result = result + d1 + d2

if d2>d1:
    if d1+d3>d2:
        result = result+d2
    else:
        result = result+d1+d3
else:
    if d2+d3>d1:
        result = result+d1
    else:
        result = result+d2+d3

print(result)











