'''
Problem statement:

Maximum sum subarray.
'''

#Naive
l = [1, 2, -3, 5, 3, -2, 3]
maxs = 0
for i in range(len(l)):
    s = 0
    for j in range(i, len(l)):
        s += l[j]
    maxs = max(maxs, s)
print(maxs)

#Kadanes
'''
We look for positive sum segments in the array.
'''
l = [1, 2, -3, 5, 3, -2, 3]
maxs = 0
curr = 0
for i in l:
    curr = max(curr+i, i)
    maxs = max(curr, i)
print(maxs)