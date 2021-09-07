'''
Problem statement:

Median of sorted arrays.
'''
nums1 = [1, 3]
nums2 = [2]
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
low = 0; high = len(nums1)
n = (len(nums1)+len(nums2)+1)//2
while (low <= high):
    l1, l2 = -10e6, -10e6
    r1, r2 = 10e6, 10e6
    cut1 = (low+high)//2
    cut2 = n - cut1
    if cut1:
        l1 = nums1[cut1-1]
    if cut2:
        l2 = nums2[cut2-1]
    if cut1 != len(nums1):
        r1 = nums1[cut1]
    if cut2 != len(nums2):
        r2 = nums2[cut2]
    if (l1 <= r2 and l2 <= r1):
        median = max(l1, l2)
        if (len(nums1) + len(nums2))%2 == 0:
            median = (median+min(r1,r2))/2
        print(median)
        break
    elif l1 > r2:
        high = cut1 - 1
    else:
        low = cut1 + 1
    