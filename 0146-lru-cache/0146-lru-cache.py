class Node:
    def __init__(self, key: int, val: int):
        # Initialize a doubly linked list node with a key-value pair
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {}  # HashMap to store key-node pairs 

        # Dummy head and tail nodes for the doubly linked list
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left  # Initialize the doubly linked list

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # Insert a node at the right (most recently used position)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # If key exists, move the node to the most recently used position
            self.remove(self.cache[key])  # Remove it from its current position
            self.insert(self.cache[key])  # Re-insert it as most recently used
            return self.cache[key].val  # its mapped like this in hashmap Key : [0,0] #node key,val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key exists, remove the old node before updating
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)  # Add or update the key-node pair
        self.insert(self.cache[key])  # Move the new/updated node to the most recently used position
        
        # Check if the cache exceeds its capacity
        if len(self.cache) > self.cap:
            lru = self.left.next  # Least recently used node (next to the dummy head)
            self.remove(lru) 
            del self.cache[lru.key] 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)