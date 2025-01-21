# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Middle (slow and fast)
        slow, fast = head, head.next
        while fast and fast.next:  # Fast moves 2 steps while slow moves 1 step
            fast = fast.next.next
            slow = slow.next
        mid = slow  # Slow now points to the middle node

        # Reverse the second half of the list
        cur = mid.next  
        mid.next = None  # Disconnect the first half from the second half
        prev = None
        while cur:  
            next_node = cur.next  # Save the next node
            cur.next = prev  # Reverse the link
            prev = cur  # Move prev forward
            cur = next_node  # Move cur forward

        # Merge the two halves
        first, second = head, prev  # `prev` points to the head of the reversed second half
        while second: 
            temp1, temp2 = first.next, second.next  # Save next nodes
            first.next = second  
            second.next = temp1  
            # thats one loop 3 nodes have been reordered
            first, second = temp1, temp2  # Move pointers forward for the next merge
