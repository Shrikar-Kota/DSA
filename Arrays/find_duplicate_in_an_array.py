'''
Problem statement:

An array of integers having one integer repeating. Range of integers is given.

example: [1 2 4 3 2 2 5 7 9 0]
output: 2, 5
'''

#Naive
'''
Sort the array and find the repeating number.
'''
l = [1, 2, 3, 4, 2, 2, 5, 6, 7]
l.sort()
r = l[0]
for i in l[1:]:
    if i == r:
        break
    r = i
print(r)

#Better
'''
Use Hashing.
'''
h = {}
l = [1, 2, 3, 4, 2, 2, 5, 6, 7]
for i in l:
    if i in h:
        print(i)
        break
    h[i] = 0

#Best
'''
We can use the concept of cycles used in linked lists.
Example:
[1 2 3 4 2 5 6 8 11]
Here since numbers dont exceed length of the array, we can treat them as indices. We see this as a linked list and use floyd's cycle detection.


1 2 3 4 2 5 can be interpreted as:

a -> b -> c -> d
     |         |
      ---------
 
so next pointer here is equivalent to the (element_value-1) 

'''
slow = l[0]
fast = l[slow-1]
while l[slow-1] != l[fast-1]:
    slow = l[slow-1]
    fast = l[fast-1]
    fast = l[fast-1]
print(fast, slow)