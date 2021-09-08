'''
Problem statement:

Find MSB.
'''

#Naive
'''
Find logarithm of number and do 2**log
'''

#Better
n = 16 #1001
k = 0
count = 0
while n > 0:
    count += 1
    n = n >> 1
print(1 << (count-1))

#Optimal
n = 16
n |= n >> 1
n |= n >> 2
n |= n >> 4
n |= n >> 8
n += 1
n = n >> 1
print(n)