'''
Problem statement:

Two variants:
- Sorted elements are put in matrix in an row-order wise.
- Rows and columns are sorted.
'''
target = 4
#first variant
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
def convertpos(pos, n):
    i = pos//(n)
    j = pos%(n)
    return (i, j)
m = len(matrix); n = len(matrix[0])
low = 0; high = m*n - 1
flag = False
while low <= high:
    pos = (low+high)//2
    i, j = convertpos(pos, n)
    if matrix[i][j] == target:
        flag = True
        break
    elif matrix[i][j] > target:
        high -= 1
    else:
        low += 1
print(flag)

#Second Variant
matrix = [[10, 20, 30, 40], [15, 25, 34, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
m = len(matrix)
n = len(matrix[0])
i = 0; j = n - 1; flag = False
while i < m and j >= 0:
    if matrix[i][j] == target:
        flag = True
        break
    if matrix[i][j] > target:
        j -= 1
    else:
        i += 1
print(flag)