'''
Problem statement:

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
'''

'''
Example:

[1, 2, 3] -> [1, 3, 2]
'''

#Naive
from itertools import permutations
l = [1, 2, 3]
d = l[:]
d.sort()
perms = perms = sorted(set(permutations(d)))
for rank in range(len(perms)):
    flag = True
    for j in range(len(l)):
        if perms[rank][j] != l[j]:
            flag = False
            break
    if flag:
        break
print(perms[(rank + 1)%len(perms)])

#optimal
index = -1
for i in range(len(l)-1, 0, -1):
    if l[i] > l[i-1]:
        index = i - 1
        break
if index == -1:
    l[:] = l[::-1]
else:
    for i in range(len(l)-1, -1, -1):
        if l[i] > l[index]:
            l[index], l[i] = l[i], l[index]
            l[index+1:] = l[index+1:][::-1]
            break
print(l)