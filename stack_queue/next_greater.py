'''
Problem statement:

Find the next greater element on right side.
'''

#naive
arr = [1, 2, 1, 3, 4, 5]
ng = [-1 for i in range(len(arr))]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            ng[i] = arr[j]
            break

print(ng)


#Optimal
stack = []
ng = [-1 for i in range(len(arr))]
for i in range(len(arr)-1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if stack:
        ng[i] = stack[-1]
    stack.append(arr[i])
print(ng)