'''
Problem statement:

Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
'''
def mergesort(nums, low, high):
    count = 0
    if low < high:
        mid = low + (high-low)//2
        count += mergesort(nums, low, mid)
        count += mergesort(nums, mid+1, high)
        count += merge(nums, low, mid, high)
    return count
def merge(nums, low, mid, high):
    a = nums[low:mid+1]
    b = nums[mid+1:high+1]
    m = len(a)
    n = len(b)
    i = 0; j = 0; k = 0; count = 0
    while i < m and j < n:                
        if a[i] > 2*b[j]:
            count += m - i
            j += 1
        else:
            i += 1
    i = 0; j = 0
    while i < m and j < n:                
        if a[i] > b[j]:
            nums[low+k] = b[j]
            j += 1
        else:
            nums[low+k] = a[i]
            i += 1
        k += 1
    while i < m:
        nums[low+k] = a[i]
        i += 1
        k += 1
    while j < n:
        nums[low+k] = b[j]
        j += 1
        k += 1
    return count
return mergesort(nums, 0, len(nums)-1)