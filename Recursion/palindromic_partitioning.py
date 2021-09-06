'''
Problem statement:

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
'''
s = "aab"
out = []
def palindromic(s, i, sets, p):
    if i == len(s):
        if p == p[::-1]:
            sets.append(p)
            out.append(sets)
        return
    if p == p[::-1]:
        palindromic(s, i + 1, sets[:], p + s[i])
        sets.append(p)
        palindromic(s, i + 1, sets, s[i])
    else:
        palindromic(s, i + 1, sets[:], p + s[i])
palindromic(s, 1, [], s[0])
print(out)