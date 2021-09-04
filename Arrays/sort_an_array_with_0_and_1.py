'''
Problem statement:

Sort an array of 0’s 1’s without using extra space or sorting algo 

'''
n = int(input())
l = list(map(int, input().split()))

#naive approach
'''
Count number of zeroes and ones. 
'''
zerocount = 0
for i in range(n):
    if l[i] == 0:
        zerocount += 1
for i in range(zerocount):
    l[i] = 0
for i in range(zerocount, n):
    l[i] = 1

print(l)

#two pointer approach

zeroptr = 0
mover = 0

for i in range(n):
    if l[i] == 0:
        l[zeroptr], l[mover] = l[mover], l[zeroptr]
        zeroptr += 1
    mover += 1

print(l)