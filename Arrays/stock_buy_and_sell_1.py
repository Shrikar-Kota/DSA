'''
Problem statement:

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Example: [7,1,5,3,6,4]
5

'''
s = [7, 1, 5, 3, 6, 4]

#Naive
maxp = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        maxp = max(maxp, s[j]-s[i])
print(maxp)

#Optimal Approach 1
maxp = 0
bp = s[0]
for i in range(1, len(s)):
    if s[i] < bp:
        bp = s[i]
    else:
        maxp = max(s[i]-bp, maxp)
print(maxp)

#Optimal Approach 2
maxp = 0
sp = s[-1]
for i in range(len(s)-2, -1, -1):
    if sp < s[i]:
        sp = s[i]
    else:
        maxp = max(sp-s[i], maxp)
print(maxp)