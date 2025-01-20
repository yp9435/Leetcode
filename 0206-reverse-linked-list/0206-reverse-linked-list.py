# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head  # Current node 
        prev = None  # Previous node starts as None since there's no node before the head

        while cur:
            next_node = cur.next  # Store the next node temporarily
            cur.next = prev  # Reverse the pointer to point to the previous node
            prev = cur  # Move the previous pointer to the current node
            cur = next_node  # Move the current pointer to the next node

        # At the end, 'prev' will be the new head of the reversed list
        return prev