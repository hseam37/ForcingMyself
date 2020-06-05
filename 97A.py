'''
https://codeforces.com/contest/96/problem/A
Author : hasanur.seam
'''
input_number = str(input())
prev = input_number[0]
count = 0 
a = False
for i in input_number:
    if(i==prev):
        count = count + 1
    else:
        count = 0
    if(count == 6):
        a = True
        break
    prev = i
if(a):
    print('YES')
else:
    print('NO')

    













