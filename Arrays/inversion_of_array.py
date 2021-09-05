'''
Problem statement:

Count the number of inversions in an array
'''

l = [3, 1, 2]
#Naive
count = 0
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            count += 1

print(count)

#Using Merge Sort
def mergesort(l, low, high):
    count = 0
    if low < high:
        mid = (low+high)//2
        count += mergesort(l, low, mid)
        count += mergesort(l, mid+1, high)
        count += merge(l, low, high, mid)
    return count
def merge(l, low, high, mid):
    a = l[low:mid+1]
    b = l[mid+1:high+1]
    i = 0; j = 0; k = 0
    count = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            l[low+k] = b[j]
            count += len(a) - i
            j += 1
        else:
            l[low+k] = a[i]
            i += 1
        k += 1
    while i < len(a):
        l[low+k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        l[low+k] = b[j]
        j += 1
        k += 1
    return count
print(mergesort(l, 0, len(l)-1))