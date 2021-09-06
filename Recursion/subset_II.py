'''
Problem statement:

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
nums = [1,2,2]
out = []
def subsets(l, i = 0, set = []):
    if i == len(l):
        out.append(set)
        return 
    k = i + 1
    while k < len(l) and l[i] == l[k]:
        k += 1
    subsets(l, k, set[:])
    set.append(l[i])
    subsets(l, i + 1, set[:])
nums.sort()    
subsets(nums)
print(out)