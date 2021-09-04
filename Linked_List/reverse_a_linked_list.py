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

#Naive method
'''
Make a new linked list
'''
head = initialize()
stack = []
while head != None:
    stack.append(head.data)
    head = head.next
head = Node(stack.pop())
temp = head
while stack:
    temp.next = Node(stack.pop())
    temp = temp.next
while head:
    print(head.data, end = "\t")
    head = head.next
print()

#Change Links 
'''
1 -> 2 -> 3 -> 4 -> 5

we maintain a previous pointer which points to the reverse linked list's gonnna be next.
Initially prev = None

None <- 1 2 -> 3 -> 4 -> 5
prev = 1

.
.
.

None <- 1 <- 2 <- 3 <- 4 <- 5
'''
head = initialize()
prev = None
while head.next:
    head.next, prev, head = prev, head, head.next
head.next = prev
while head:
    print(head.data, end = "\t")
    head = head.next
    