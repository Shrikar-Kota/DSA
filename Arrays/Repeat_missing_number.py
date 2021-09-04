'''
Problem statement:

One number missing and one number repeats twice in an array of integers ranging from 1 to N.
Find the repeating and missing.

example: [1 2 4 3 2]
output: 2, 5
'''

#updating the array
'''
[1 2 4 3 2] rn = 0, ms = 0
[-1 2 4 3 2] rn = 0, ms = 0
[-1 -2 4 3 2] rn = 0, ms = 0
[-1 -2 4 -3 2] rn = 0, ms = 0
[-1 -2 -4 -3 2] rn = 0, ms = 0
[-1 -2 -4 -3 2] rn = 2, ms = 0

Traverse the array again and check for positive number. Positive number index + 1 = missing number.
rn = 2, ms = 5
'''
l = [1, 2, 4, 3, 2]
rn = 0; ms = 0
for i in l:
    if l[abs(i)-1] < 0:
        rn = abs(i)
    else:
        l[abs(i)-1] = -l[abs(i)-1]
for i in range(len(l)):
    if l[i] > 0:
        ms = i + 1
print(rn, ms)

#using hashing
l = [1, 2, 4, 3, 2]
rn = 0; ms = 0
h = {i+1:0 for i in range(len(l))}
for i in l:
    if h[i] > 0:
        rn = i
    else:
        h[i] += 1
for i in h:
    if h[i] == 0:
        ms = i
        break
print(ms, rn)

#using xor
'''
find xor of all numbers. find xor of all elements. find xor of xors. resultant xor is ms ^ rn. classify the numbers into 2 sets. 
'''

xor = 0
l = [1, 3, 4, 3, 2]
rn = 0; ms = 0
for i in range(1, len(l)+1):
    xor = xor ^ i
for i in l:
    xor = xor ^ i
xor = xor - (xor & (xor-1))
for i in l:
    if xor & i:
        rn = rn^i 
    else:
        ms = ms^i
for i in range(1, len(l)+1):
    if xor & i:
        rn = rn^i 
    else:
        ms = ms^i
print(rn,ms)