'''
Problem statement:

Implement stack using array.
'''

class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1
    def push(self, data):
        self.stack.append(data)
stack = Stack()
