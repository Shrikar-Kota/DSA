'''
Problem statement:

Merge Two Sorted Arrays
'''

l1 = [1, 2, 3, 4, 5, 6]
l2 = [2, 3, 5, 7, 9]

#Naive(Extra Space) -NlogN (N = m + n)
l3 = [i for i in l1]
for i in l2:
    l3.append(i)
l3.sort()
for i in range(len(l1)):
    l1[i] = l3[i]
for i in range(len(l1), len(l1)+len(l2)):
    l2[i-len(l1)] = l3[i]
print(l1)
print(l2)
#Naive(Extra Space) - O(n.m)
l1 = [1, 2, 3, 4, 5, 6]
l2 = [2, 3, 5, 7, 9]
i = 0
while i < len(l1):
    if l1[i] <= l2[0]:
        i += 1
    else:
        l1[i], l2[0] = l2[0], l1[i]
        j = 1; ele = l2[0]
        while j < len(l2):
            if l2[j] <= ele:
                l2[j-1] = l2[j]
            else:
                break
            j += 1
        l2[j-1] = ele
print(l1)
print(l2)
        
#Shell Sort