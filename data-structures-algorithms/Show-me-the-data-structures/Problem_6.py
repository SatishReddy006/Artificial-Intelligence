#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    s = set()
    current = llist_1.head
    while current:
        s.add(current.value)
        current = current.next
    current = llist_2.head
    while current:
        s.add(current.value)
        current = current.next

    result = LinkedList()
    for num in s:
        result.append(num)
    return result


def intersection(llist_1, llist_2):
    # Your Solution Here
    s1 = set()
    current = llist_1.head
    while current:
        s1.add(current.value)
        current = current.next

    s2 = set()
    current = llist_2.head
    while current:
        s2.add(current.value)
        current = current.next

    temp_list = sorted([s1, s2], key=len)
    s = set()

    for ele in temp_list[0]:
        if ele in temp_list[1]:
            s.add(ele)

    result = LinkedList()
    for num in s:
        result.append(num)
    return result


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))  #return 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2)) #return 4 -> 21 -> 6 ->

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  #return 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
print(intersection(linked_list_3, linked_list_4)) #return 


# Test case 3
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

print(union(linked_list_3, linked_list_4))  #return 
print(intersection(linked_list_3, linked_list_4)) #return 


# Test case 4
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  #return 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print(intersection(linked_list_3, linked_list_4)) #return 