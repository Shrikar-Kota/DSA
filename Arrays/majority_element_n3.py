'''
Problem statement:

Two elements occurs more than n/3 times. Find the elements.
'''

#Naive
l = [2, 2, 3, 3, 2, 2]
els = []
for i in range(len(l)):
    count = 0
    for j in range(len(l)):
        if  l[i] == l[j]:
            count += 1
    if count > len(l)//3 and l[i] not in els:
        els.append(l[i])
print(els)

#Optimal
l = [2, 2, 3, 3, 2, 2]
els = []
h = {}
for i in range(len(l)):
    if l[i] in h:
        h[l[i]] += 1
    else:
        h[l[i]] = 1
    if h[l[i]] > len(l)//3 and l[i] not in els:
        els.append(l[i])
print(els)
