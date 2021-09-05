'''
Problem statement:

You are given an n x n 2D matrix, rotate the matrix by 90 degrees (clockwise).

1 2 3        7 4 1
4 5 6  --->  8 5 2
7 8 9        9 6 3
'''

#Naive
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
temp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        temp[j][len(matrix[0])-i-1] = matrix[i][j]
print(temp)

#Without extra space
'''
Transpose and reverse elements of each row

1 2 3                   1 4 7                       7 4 1
4 5 6   -->Transpose    2 5 8   -->Reverse Row      8 5 2
7 8 9                   3 6 9                       9 6 3
'''
for i in range(len(matrix)):
    for j in range(i, len(matrix[0])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
print(matrix)