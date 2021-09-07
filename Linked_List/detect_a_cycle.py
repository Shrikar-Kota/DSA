'''
Problem statement:

Given a Linked List. Tell if it contains a cycle or not.
'''

#Naive
'''
Have a hashmap which stores the references of the nodes.
'''

#Optimal
'''
Manipulate the Node and add a visited attribute.
'''

#Cycle detection
slow = head
fast = head
while slow and fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return True
