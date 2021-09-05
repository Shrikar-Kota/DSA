'''
Problem statement:

An element occurs more than n/2 times. Find the element.
'''

#Naive
l = [2,2,1,1,1,2,2]
majority = -1
for i in range(len(l)):
    count = 0
    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1
    if count > len(l)//2:
        majority = l[i]
        break
print(majority)

#Better
l = [2,2,1,1,1,2,2]
l.sort()
print(l[len(l)//2])

#Optimal
h = {}
majority = -1
for i in l:
    if i in h:
        h[i] += 1 
    else:
        h[i] = 1
    if h[i] > len(l)//2:
        majority = i
        break
print(majority)       

#Moorey-Voting
majority = -1
count = 0
for i in l:
    if count == 0:
        majority = i
        count = 1
    elif majority == i:
        count += 1
    else:
        count -= 1
print(majority)

#Bits
arr = [0 for i in range(32)]
for i in range(32):
    for j in l:
        if (1 << i) & j:
            arr[i] += 1
majority = 0
for i in range(32):
    if arr[i] > len(l)/2:
        majority = majority | 1 << i

print(majority)