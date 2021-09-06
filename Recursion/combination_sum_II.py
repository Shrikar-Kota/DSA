'''
Problem statement:

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
'''
candidates = [10,1,2,7,6,1,5]; target = 8
out = []
def getcount(candidates, target, sum = 0, i = 0, sets = []):
    if sum > target or i == len(candidates):
        if sum == target:
            out.append(sets)
        return
    if target == sum:
        out.append(sets)
        return
    k = i + 1
    while k < len(candidates) and candidates[i] == candidates[k]:
        k += 1
    getcount(candidates, target, sum, k, sets[:])
    sets.append(candidates[i])
    getcount(candidates, target, sum + candidates[i], i + 1, sets[:])
    return
getcount(sorted(candidates), target)
print(out)
