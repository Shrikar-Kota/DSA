'''
Problem statement:

Power of 2
'''

#Naive
n = 15
import math
if 2**(math.log2(n)) == n:
    print("True")
else:
    print("False")

#Better
count = 0
n = 15
while n > 0:
    if n&1:
        count += 1
    n = n >> 1
if count == 1:
    print("True")
else:
    print("False")

#Best
n = 15
if n&(n-1) == 0:
    print("True")
else:
    print("False")

