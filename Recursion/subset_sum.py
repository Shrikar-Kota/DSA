'''
Problem Statement:

Given a list arr of N integers, print sums of all subsets in it.
'''

l = [5, 2, 1]

def subsetsum(l, i = 0, sums = [], sum = 0):
    if i == len(l):
        sums.append(sum)
        return sums
    sums = subsetsum(l, i + 1, sums, sum + l[i])
    sums = subsetsum(l, i + 1, sums, sum)
    return sums

print(subsetsum(l))