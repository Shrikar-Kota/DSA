'''
Problem statement:

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
'''
#Naive
'''
For every node in ListA check if this node exists in ListB
'''

#Optimal
'''
Use a hashmap and store the addresses
'''

#Optimal
def getIntersectionNode(headA, headB):
    lengthA = 0
    lengthB = 0
    temp = headA
    while temp:
        lengthA += 1
        temp = temp.next
    temp = headB
    while temp:
        lengthB += 1
        temp = temp.next
    if lengthA > lengthB:
        diff = lengthA - lengthB
        while diff:
            headA = headA.next
            diff -= 1
    else:
        diff = lengthB - lengthA
        while diff:
            headB = headB.next
            diff -= 1
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None