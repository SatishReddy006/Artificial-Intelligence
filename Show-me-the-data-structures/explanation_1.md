Explanation: LRU Cache

LRU cache implemented using maps and doubly linked list. Map is used to retrieve elements and doubly linked list helps to retrieve items in order of recency.Recent updated/insterted/accessed element stored in head of linked list and least frequently element stored at end of linked list. Removing last element of linked list when cpacity is reached.

Time complexity of get() or set() is O(1). Space complexity is O(n)