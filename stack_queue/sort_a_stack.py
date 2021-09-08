'''
Problem statement:

Sort a stack.
'''

#Naive
stack = [2, 5, 8, 3, 1, 2, 4]
arr = []
while stack:
    arr.append(stack.pop())
arr.sort()
for i in arr:
    stack.append(i)
print(stack)
#using a stack
stack = [2, 5, 8, 3, 1, 2, 4]
temp = []
def sortstack(s):
    if len(s) != 0:
        temp = stack.pop(0)
        sortstack(stack)
        sortedinsert(stack, temp)
def sortedinsert(s, data):
    if len(s) == 0 or stack[-1] >= data:
        stack.append(data)
        return
    temp = stack.pop()
    sortedinsert(stack, data)
    sortedinsert(stack, temp)
sortstack(stack)
print(stack)