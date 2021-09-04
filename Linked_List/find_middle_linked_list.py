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
'''
We store the values in array and print middle.
'''

arr = []
head = initialize()
while head:
    arr.append(head.data)
    head = head.next
print(arr[len(arr)//2])

#Best
'''
Maintain two pointers. One fast, one slow. Fast moves double the speed.
'''

head = initialize()
fast = head
slow = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
print(slow.data)