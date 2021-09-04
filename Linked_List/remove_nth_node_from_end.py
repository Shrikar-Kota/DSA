'''
Problem statement:

Reverse a linked list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def initialize():
    head = Node(0)
    temp = head
    for i in range(1, 10):
        temp.next = Node(i)
        temp = temp.next
    return head

#Naive
head = initialize()
arr = []
n = 5
temp = head
while temp:
    arr.append(temp)
    print(temp.data, end = "\t")
    temp = temp.next
print()
if n == len(arr):
    head = arr[1] if len(arr) > 1 else None
elif n == 1:
    if len(arr) > 1:
        arr[len(arr)-2].next = None
    else:
        head = None
else:
    arr[len(arr)-n-1].next = arr[len(arr)-n+1]
while head:
    print(head.data, end = "\t")
    head = head.next
print()

#Better
'''
1 -> 2 -> 3 -> 5 -> 6 -> 7

3rd from last

- move the start pointer 4 steps

- start at 5

- now start slow pointer till start reaches end i.e. 2 steps.

- slow.next = None

'''
