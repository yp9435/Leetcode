# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        # Variable to keep track of carry for digits summing more than 9
        carry = 0
        
        # Iterate as long as there are nodes in l1, l2, or a carry exists
        while l1 or l2 or carry:
            # Get values from current nodes of l1 and l2, or 0 if the node is None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Calculate the sum of the digits and the carry
            val = v1 + v2 + carry
            carry = val // 10  # Update carry for the next addition
            val = val % 10     # Value for the current node

            # Create a new node with the computed value and move the pointer
            cur.next = ListNode(val)
            
            # Update pointers 
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next