'''
Problem statement:

Find the next smaller element.
'''

#Naive

arr = [1, 2, 1, 3, 4, 5]
ns = [-1 for i in range(len(arr))]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            ns[i] = arr[j]
            break
print(ns)

#Optimal
arr = [1, 2, 1, 3, 4, 5]
ns = [-1 for i in range(len(arr))]
stack = []
for i in range(len(arr)-1, -1, -1):
    while stack and stack[-1] >= arr[i]:
        stack.pop()
    if stack:
        ns[i] = stack[-1]
    stack.append(arr[i])
print(ns)