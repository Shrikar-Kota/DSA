'''
Problem statement:

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
Inplace
'''

m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

#Naive approach O(m*n*(m+n))
INT_MIN = -(2**31 + 1)
def makezero(matrix, i, j):
    for x in range(len(matrix)):
        if matrix[x][j] != 0:
            matrix[x][j] = INT_MIN
    for x in range(len(matrix[0])):
        if matrix[i][x] != 0:
            matrix[i][x] = INT_MIN
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 0:
            makezero(m, i, j)
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == INT_MIN:
            m[i][j] = 0
print(m)

#Better
'''
Instead updating right away, we maintain two arrays indicating row zero and column zero.
'''
m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
x_axis = [1 for i in range(len(m[0]))]
y_axis = [1 for i in range(len(m))]
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 0:
            y_axis[i] = 0
            x_axis[j] = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if y_axis[i] == 0 or x_axis[j] == 0:
            m[i][j] = 0
print(m)
#Best(No extra space)
'''
Instead of using extra space, we use the first row and column as our row zero and column zero.
'''
m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
first_row = False
first_column = False
for i in range(len(m)):
    if m[i][0] == 0:
        first_column = True
        break
for j in range(len(m[0])):
    if m[0][j] == 0:
        first_row = True
        break
for i in range(1, len(m)):
    for j in range(1, len(m[0])):
        if m[i][j] == 0:
            m[0][j] = 0
            m[i][0] = 0
for i in range(1, len(m)):
    for j in range(1, len(m[0])):
        if m[0][j] == 0 or m[i][0] == 0:
            m[i][j] = 0

if first_row:
    for j in range(len(m[0])):
        m[0][j] = 0
if first_column:
    for i in range(len(m)):
        m[i][0] = 0
print(m)