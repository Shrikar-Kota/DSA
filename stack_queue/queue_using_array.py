'''
Problem statement:

Implement queues using arrays.
'''

class Queue:
    def __init__(self, n):
        self.queue = [0 for i in range(n)]
        self.front = -1
        self.end = -1
        self.size = n
    def enqueue(self, data):
        if self.front == (self.end+1)%self.size:
            print("Overflow")
            return
        self.end = (self.end + 1)%self.size
        self.queue[self.end] = data
        if self.front == -1:
            self.front = self.end
    def dequeue(self):
        if self.end == -1:
            print("Underflow")
            return
        out = self.queue[self.front]
        self.queue[self.front] = 0
        if self.front == self.end:
            self.front = self.end = -1
        else:
            self.front = (self.front+1)%self.size
        print("Dequeued",out)
        return
    def print(self):
        if self.front == -1:
            print("Underflow")
            return
        temp = self.front
        while temp != self.end:
            print(self.queue[temp], end = "\t")
            temp = (temp+1)%self.size
        print(self.queue[temp])

    
queue = Queue(5)
queue.enqueue(4)
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.print()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.print()
queue.dequeue()
queue.print()
queue.enqueue(2)
queue.print()
queue.enqueue(4)
queue.enqueue(1)
queue.enqueue(3)
queue.dequeue()
queue.print()