'''
Problem statement:

Divide integers without using /.
'''

#Naive
n = 6
m = 2
count = 0
while n >= m:
    n -= m
    count += 1
print(count)

#Optimal
n = 6
m = 2

n = n >> 1

print(n)