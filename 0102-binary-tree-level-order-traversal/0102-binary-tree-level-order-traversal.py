# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] 
        q = collections.deque()  
        q.append(root) 

        while q: 
            qlen = len(q)  # Number of nodes at the current level
            level = [] 

            for i in range(qlen):  # Process all nodes at the current level
                node = q.popleft() 
                if node: 
                    level.append(node.val)  
                    q.append(node.left)  # Add left child to the queue
                    q.append(node.right)  # Add right child to the queue
            
            if level:  
                result.append(level)
        
        return result  