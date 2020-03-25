'''
https://codeforces.com/problemset/problem/266/A
Author: Arrow
'''

n = int(input())

l = list(input())

r = 0

for i in range(len(l)-1):
    if l[i]==l[i+1]:
        r += 1

print(r)
