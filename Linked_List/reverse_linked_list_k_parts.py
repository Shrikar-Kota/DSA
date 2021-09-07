'''
Problem statement:

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
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
k = 3
n = 0
arr = []
temp = head
ptr = head
while temp:
    if n == k:
        while ptr != temp:
            ptr.data = arr.pop()
            n -= 1
            ptr = ptr.next
    arr.append(temp.data)
    temp = temp.next
    n += 1
if n == k:
    while ptr != temp:
        ptr.val = arr.pop()
        n -= 1
        ptr = ptr.next
while head:
    print(head.data, end = " -> ")
    head = head.next

#Without swapping data