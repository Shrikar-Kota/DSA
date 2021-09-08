'''
Problem statement:

Find the nearest greater element in circular fashion.
'''

arr = [1, 2, 1, 3, 4, 5]
ng = [-1 for i in range(len(arr))]
for i in range(len(arr)):
    j = (i + 1)%len(arr)
    while j != i:
        if arr[j] > arr[i]:
            ng[i] = arr[j]
            break
        j = (j+1)%len(arr)

print(ng)

#Better
stack = []
arr.extend(arr)
ng = [-1 for i in range(len(arr)//2)]
for i in range(len(arr)-1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if i < len(arr)//2:        
        if stack:
            ng[i] = stack[-1] 
    stack.append(arr[i]) 
print(ng)      

