# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Floyd's Cycle Detection Algorithm (Tortoise and Hare approach)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()  # Create a dummy node to handle edge cases
        dummy.next = head
        slow = fast = dummy  # Initialize two pointers: slow and fast

        while fast and fast.next:  # Continue until fast pointer reaches the end
            fast = fast.next.next  # Move fast pointer 2 steps 
            slow = slow.next       # Move slow pointer 1 step 

            if slow is fast:       # If slow and fast meet, there's a cycle
                return True

        return False  # If no cycle is detected, return False