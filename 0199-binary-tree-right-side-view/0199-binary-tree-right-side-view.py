# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])  # Initialize queue with root node

        while q:
            rightSide = None  # Keeps track of the rightmost node at each level
            qLen = len(q)  # Get the number of nodes at the current level

            for i in range(qLen):  
                node = q.popleft()  # Pop the next node in the queue
                
                if node:
                    rightSide = node  # Update rightSide to the latest node at this level
                    q.append(node.left)  # Add left child first
                    q.append(node.right)  # Then add right child

            if rightSide:
                res.append(rightSide.val)  # Store the rightmost node's value

        return res  # Return the list of rightmost nodes