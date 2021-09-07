'''
Problem statement:

Find nth root of a number.
'''

#naive
m = 4
n = 2
print(4**(1/n))

#Binary search
low = 1
high = m
while (high-low) > 10**(-6):
    mid = low + (high-low)/2
    if (mid**n == m):
        break
    if (mid**n < m):
        low = mid
    else:
        high = mid
print(mid)