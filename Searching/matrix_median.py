'''
Problem statement:

Given a matrix of integers A of size N x M in which each row is sorted.

Find an return the overall median of the matrix A.
'''

#Naive
m = [   
        [1, 3, 6],
        [2, 6, 9],
        [3, 6, 9]
    ]
d = []
for i in m:
    for j in i:
        d.append(i)
    
d.sort()
print(d[len(d)//2])

#Optimal
