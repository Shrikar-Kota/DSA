'''
Problem statement:


'''

#Optimal
class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val: int):
        if self.aux:
            if self.aux[-1] >= val:
                self.aux.append(val)
        else:
            self.aux.append(val)
        self.stack.append(val)
    def pop(self):
        if self.stack:
            if self.aux[-1] == self.stack[-1]:
                self.aux.pop()
            return self.stack.pop()
        return -1
    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self):
        if self.aux:
            return self.aux[-1]
        return -1

#Best
