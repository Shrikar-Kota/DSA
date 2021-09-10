'''
Problem statement:

Find largest rectangular area.
'''

#naive
l = [2,1,5,6,2,3]
area = [1 for i in range(len(l))]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            break
        area[i] += 1
for i in range(len(l)):
    for j in range(i-1, -1, -1):
        if l[i] > l[j]:
            break    
        area[i] += 1
    area[i] *= l[i]

print(max(area))

#Better 2 pass
stack = []
areas = [1 for i in range(len(l))]
for i in range(len(l)-1, -1, -1):
    while stack and l[stack[-1]] >= l[i]:
        stack.pop()
    if stack:
        areas[i] += stack[-1] - i - 1
    else:
        areas[i] += len(l) - i - 1
    stack.append(i)
stack = []
for i in range(len(l)):
    while stack and l[stack[-1]] >= l[i]:
        stack.pop()
    if stack:
        areas[i] += i - stack[-1] - 1
    else:
        areas[i] += i
    stack.append(i)
    areas[i] *= l[i]
print(max(areas))

#Best
stack = []
areas = [1 for i in range(len(l))]
for i in range(len(l)-1, -1, -1):
    while stack and l[stack[-1]] >= l[i]:
        x = stack.pop()
        areas[] += x - i
    if stack:
        areas[i] += stack[-1] - i - 1
    else:
        areas[i] += len(l) - i - 1
    stack.append(i)
print(areas)
    