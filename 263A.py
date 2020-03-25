'''
https://codeforces.com/problemset/problem/263/A
Author: Arrow
'''
def getInitailPosition(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j]==1:
                pos = [i,j]
                return pos

def getResult(initialPosition):
    result = abs(2-initialPosition[0])+abs(2-initialPosition[1])
    return result

matrix = []

for i in range(5):
    a = list(map(int,input().split()))
    matrix.append(a)

initialPosition = getInitailPosition(matrix)

print(getResult(initialPosition))


