'''
Problem statement:

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
'''
candidates = [2,3,6,7]
target = 7
def getcount(candidates,target,s=0,out =[],i=0,outs=[]):
    if i == len(candidates) or s > target:
        if target == s:
            print(out)
        return
    if target == s:
        print(out)
        return
    getcount(candidates, target, s, out[:], i+1)
    out.extend([candidates[i]])
    getcount(candidates, target, s+candidates[i], out, i)
    return

getcount(candidates, target)