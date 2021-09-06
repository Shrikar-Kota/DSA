'''
Problem statement:

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
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

head = initialize()

def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next

deleteNode(head.next)

while head:
    print(head.data, end = "\t")
    head = head.next