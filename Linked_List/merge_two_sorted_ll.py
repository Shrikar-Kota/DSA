'''
Problem statement:

Merge two sorted linked lists
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def initialize():
    l1 = [1, 2, 3, 4, 4, 5]
    l2 = [1, 2, 3, 3, 4, 5, 6, 8, 8]
    head1 = Node(0); head2 = Node(0)
    temp = head1
    for i in l1:
        temp.next = Node(i)
        temp = temp.next
    temp = head2
    for i in l2:
        temp.next = Node(i)
        temp = temp.next
    return head1, head2

#Naive
'''
Store them in an array and sort them.
'''
arr = []
head1, head2 = initialize()
while head1:
    arr.append(head1.data)
    head1 = head1.next
while head2:
    arr.append(head2.data)
    head2 = head2.next
arr.sort()
head1 = Node(arr[0])
temp = head1
for i in arr[1:]:
    temp.next = Node(i)
    temp = temp.next
while head1:
    print(head1.data, end = "\t")
    head1 = head1.next
print()

#Optimal
'''
Use Merge Sort's Merge technique(Extra space)
'''

mhead = None
ptr = None
head1, head2 = initialize()
while head1 and head2:
    if head1.data > head2.data:
        if mhead:
            ptr.next = Node(head2.data)
            head2 = head2.next
            ptr = ptr.next
        else:
            mhead = Node(head2.data)
            head2 = head2.next
            ptr = mhead
    else:
        if mhead:
            ptr.next = Node(head1.data)
            head1 = head1.next
            ptr = ptr.next
        else:
            mhead = Node(head1.data)
            head1 = head1.next
            ptr = mhead
while head1:
    ptr.next = Node(head1.data)
    head1 = head1.next
    ptr = ptr.next
while head2:
    ptr.next = Node(head2.data)
    head2 = head2.next
    ptr = ptr.next
while mhead:
    print(mhead.data, end = "\t")
    mhead = mhead.next
print()

'''
Use Merge Sort's Merge technique(No extra space)
1 -> 2 -> 3 -> 4 -> 5
3 -> 4 -> 5 -> 6

'''
head1, head2 = initialize()
mhead = None; ptr = None
while head1 and head2:
    if head1.data > head2.data:
        if mhead:
            ptr.next = head2
            head2 = head2.next
            ptr = ptr.next
        else:
            mhead = head2
            head2 = head2.next
            ptr = mhead
    else:
        if mhead:
            ptr.next = head1
            head1 = head1.next
            ptr = ptr.next
        else:
            mhead = head1
            head1 = head1.next
            ptr = mhead
while head1:
    ptr.next = head1
    head1 = head1.next
    ptr = ptr.next
while head2:
    ptr.next = head2
    head2 = head2.next
    ptr = ptr.next
while mhead:
    print(mhead.data, end = "\t")
    mhead = mhead.next
print()