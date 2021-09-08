'''
Problem statement:

Implement queue using stack.
'''

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, data): #O(n)
        self.stack2 = self.stack1.copy()
        self.stack1.clear()
        self.stack1.append(data)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    def dequeue(self): #O(1)
        if self.stack1: 
            return self.stack1.pop()
        return -1

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
queue.enqueue(3)
print(queue.dequeue())

'''
O(1) amortized method is also possible. There we maintain two stacks.
Whenever a pop is encountered, then we check if second stack is empty. If it isnt, then element is popped. If it is then elements of stack 1 are transferred to stack2.
'''


