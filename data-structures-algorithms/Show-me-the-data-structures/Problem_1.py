#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
  def __init__(self, key, val):
    self.next = None
    self.prev = None
    self.key = key
    self.val = val

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.n = capacity
        self.count = 0
        self.nodes = {}
        self.start = None
        self.end = None
        

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.nodes.get(key)
        if not node:
            return -1
        self.move_to_front(node)
        return node.val
        

    def set(self, key, val):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.n != None and self.n>0:
            node = self.nodes.get(key)
            
            if node:
                # Update existing node and move to front
                node.val = val
                self.move_to_front(node)
                return
        
            if self.count == self.n:
                # No space, so remove last item
                if self.end:
                    del self.nodes[self.end.key]
                    self.remove(self.end)
            else:
                self.count += 1
        
            # Finally create and insert the new node
            node = Node(key, val)
            self.insert(node)
            self.nodes[key] = node
    
    def insert(self, node):
        if not self.end:
            self.end = node
        if self.start:
            node.next = self.start
            self.start.prev = node
        self.start = node

    def remove(self, node):
        if node.prev:
          node.prev.next = node.next
        if node.next:
          node.next.prev = node.prev
        if self.start == node:
          self.start = node.next
        if self.end == node:
          self.end = node.prev

    def move_to_front(self, node):
        # Remove node and re-insert at head
        self.remove(node)
        self.insert(node)

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1
print(our_cache.get(None))       # return -1

cache = LRU_Cache(2) # Limit of 2 items

cache.set('user1', 'Alex')
cache.set('user2', 'Brian')
cache.set('user3', 'Chris')

print(cache.get('user1'))   # return -1
print(cache.get('user2')) # returns Brian
print(cache.get('user3')) # returns Chris

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


our_cache = LRU_Cache(-1)
our_cache.set(1, 1);
print(our_cache.get(1))       # returns -1


our_cache = LRU_Cache(-10)
our_cache.set(1, 1);
print(our_cache.get(1))       # returns -1

our_cache = LRU_Cache(None)
our_cache.set(1, 1);
print(our_cache.get(1))       # returns -1
