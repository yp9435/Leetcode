# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        L = dummy  # track the node before the one to be removed
        R = head   # Pointer to move 'n' steps ahead

        # Move R 'n' steps forward to create a gap of 'n' nodes between L and R
        while n > 0 and R:
            R = R.next
            n -= 1

        # Move both pointers until R reaches the end, maintaining the gap
        while R:
            L = L.next
            R = R.next

        # Skip the 'nth' node from the end by changing the next pointer of L
        L.next = L.next.next

        return dummy.next