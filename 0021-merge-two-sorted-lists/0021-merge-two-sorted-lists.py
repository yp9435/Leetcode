# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        
        # Traverse both lists until one of them is exhausted
        while list1 and list2:
            # Compare the current nodes of both lists
            if list1.val < list2.val:
                cur.next = list1  # Attach the smaller node to the merged list
                list1, cur = list1.next, list1  # Move to the next node in list1
            else:
                cur.next = list2  
                list2, cur = list2.next, list2 
        
        # If any list has remaining nodes, attach them to the merged list
        if list1 or list2:
            cur.next = list1 if list1 else list2
        
        # Return the merged list starting from the node after the dummy
        return dummy.next