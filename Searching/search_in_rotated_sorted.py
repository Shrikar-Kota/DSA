'''
Problem statement:

Search in sorted rotated array.
'''

#Naive
'''
Linear Search
'''

#Optimal
'''
Use Modified Binary search.
'''
l = [4,5,6,7,0,1,2]
target = 4
low = 0; high = len(l) - 1
index = -1
while low <= high:
    mid = (low+high)//2
    if l[mid] == target:
        index = mid
        break
    if l[mid] > l[high]:
        if target >= l[low] and target <= l[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if target >= l[mid] and target <= l[high]:
            low = mid + 1
        else:
            high = mid - 1
print(index)