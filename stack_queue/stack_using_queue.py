'''
Problem statement:

Implement stack using queue.
'''
from collections import deque
#Naive
class Stack:
    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])
    def push(self, data): #O(n)
        self.queue2 = self.queue1.copy()
        self.queue1.clear()
        self.queue1.append(data)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
    def pop(self): #O(1)
        if self.queue1: 
            return self.queue1.popleft()
        return -1
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())

#Using one queue
class Stack:
    def __init__(self):
        self.queue1 = deque([])
    def push(self, data): #O(n)
        size = len(self.queue1)
        self.queue1.append(data)
        while size:
            self.queue1.append(self.queue1.popleft())
            size -= 1
    def pop(self): #O(1)
        if self.queue1: 
            return self.queue1.popleft()
        return -1
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())