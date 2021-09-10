'''
Problem statement:

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
'''
from collections import deque

class Node():
    def __init__(self, key, value):
        self.value = value
        self.prev = None
        self.next = None
        self.key = key
class DLL():
    def __init__(self):
        self.head = None
        self.tail = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = DLL()
        self.size = 0
        self.data = {}
    def get(self, key):
        if key in self.data:
            self.put(key, self.data[key].value)
            return self.data[key].value
        return -1
    def put(self, key, value):
        if key in self.data:
            if self.cache.head == self.data[key]:
                if self.size == 1:
                    self.cache.head = self.cache.tail = None
                else:
                    self.cache.head = self.cache.head.next
                    self.cache.head.prev = None
            elif self.cache.tail == self.data[key]:
                self.cache.tail = self.cache.tail.prev
                self.cache.tail.next = None
            else:
                self.data[key].next.prev = self.data[key].prev
                self.data[key].prev.next = self.data[key].next
            self.size -= 1
            self.data.pop(key)
        if self.size == self.capacity:
            self.data.pop(self.cache.head.key)
            self.cache.head = self.cache.head.next
            self.size -= 1
        if self.size == 0:
            self.cache.head = self.cache.tail = Node(key, value)
        else:
            self.cache.tail.next = Node(key, value)
            self.cache.tail.next.prev = self.cache.tail
            self.cache.tail = self.cache.tail.next
        self.size += 1
        self.data[key] = self.cache.tail
        