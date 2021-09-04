'''
Problem statement:

Sort an array of 0’s 1’s 2’s without using extra space or sorting algo 

'''
#naive approach
'''
Count number of zeroes, ones, twos. 
'''
l = [0, 1, 2, 1, 0, 2, 1, 0, 1]
zerocount = 0
onecount = 0
for i in range(len(l)):
    if l[i] == 0:
        zerocount += 1
    elif l[i] == 1:
        onecount += 1
for i in range(zerocount):
    l[i] = 0
for i in range(zerocount, zerocount+onecount):
    l[i] = 1
for i in range(zerocount+onecount, len(l)):
    l[i] = 2
print(l)

#three pointer approach/dutch flag algorithm.
'''
We maintain three pointers, one for zero, one for two and the other one traversing.
Whenever we encounter a zero, then we swap zero with traverse and increment traverse and zero.
Whenever we encounter a two, we swap and decrement two.

l = [0 1 2 1 0 2]
z = 0 t = 0 e = 5
l = [0 1 2 1 0 2]
z = 1 t = 1 e = 5
l = [0 1 2 1 0 2]
z = 1 t = 2 e = 5
l = [0 1 2 1 0 2]
z = 1 t = 2 e = 4
l = [0 1 0 1 2 2]
z = 1 t = 2 e = 3
l = [0 0 1 1 2 2]
z = 2 t = 3 e = 3
'''
l = [0, 1, 2, 1, 0, 2]
z = 0; t = 0; e = len(l) - 1

while t <= e:
    if l[t] == 1:
        t += 1
    elif l[t] == 0:
        l[z], l[t] = l[t], l[z]
        z += 1
        t += 1
    else:
        l[e], l[t] = l[t], l[e]
        e -= 1
print(l)