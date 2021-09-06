'''
Problem statement:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

Example:
l1 = [2,4,3], l2 = [5,6,4]
output: [7,0,8]
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def initialize():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    head1 = Node(l1[0]); head2 = Node(l2[0])
    temp = head1
    for i in l1[1:]:
        temp.next = Node(i)
        temp = temp.next
    temp = head2
    for i in l2[1:]:
        temp.next = Node(i)
        temp = temp.next
    return head1, head2

first, second = initialize()

def addTwoNumbers(first, second):
    carry = 0; prev = None; head = first
    while first and second:
        sum = first.data + second.data + carry
        first.data = sum%10
        carry = sum//10
        prev = first
        first = first.next
        second = second.next
    if second:
        prev.next = second
    temp = prev
    prev = prev.next
    while carry and prev:
        sum = prev.data + carry
        carry = sum//10
        prev.data = sum%10
        temp = prev
        prev = prev.next
    
    if carry:
        temp.next = Node(carry)
    return head

first = addTwoNumbers(first, second)

while first:
    print(first.data, end="")
    first = first.next
