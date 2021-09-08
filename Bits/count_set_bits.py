'''
Problem statement:

Count total set bits in a number.
'''

#Naive
count = 0
n = 15
while n:
    if n&1:
        count += 1
    n = n >> 1
print(count)

#Better
count = 0
n = 15
while n:
    count += 1
    n = n&(n-1)
print(count)