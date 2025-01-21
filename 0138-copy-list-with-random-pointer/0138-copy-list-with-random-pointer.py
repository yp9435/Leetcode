"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to map old nodes to their corresponding copies
        oldtocopy = {None: None}

        # First pass: Create a copy of the current node and store it in hashmap
        cur = head
        while cur:
            copy = Node(cur.val) # note this syntax
            oldtocopy[cur] = copy
            cur = cur.next

        # Second pass: Link the copied nodes using the hashmap
        cur = head
        while cur:
            # Get the copy of the current node
            copy = oldtocopy[cur]
            copy.next = oldtocopy[cur.next]
            copy.random = oldtocopy[cur.random]
            cur = cur.next  

        # Return the head of the copied linked list
        return oldtocopy[head]