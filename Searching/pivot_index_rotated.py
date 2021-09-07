'''
Problem statement:

Find the point of rotation of sorted array.
'''

l = [6, 7, 8, 0, 1, 2, 5]

#Naive
for i in range(len(l)):
    if l[i] < l[(i+len(l)-1)%(len(l))] and l[i] < l[(i+1)%(len(l))]:
        break
print(i)

#Optimal
low = 0; high = len(l) - 1
while low <= high:
    mid = (low + high)//2
    if (l[low] < l[mid] and l[high] > l[mid]) or l[low] > l[mid]:
        high = mid - 1
    else:
        low = mid + 1
print(mid)

#Better
'''
If the right part is sorted we move to the left part. Because there is no possibility for the smallest to be on right.
If the right part is not sorted, then our mid can be the pivot.
'''
n = len(l) - 1
low = 0; high = n
while low < high:
    mid = low + (high-low)//2
    if l[mid] > l[high]:
        low = mid + 1
    else:
        high = mid
print(l[low])