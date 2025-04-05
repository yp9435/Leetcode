# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Helper function
        def dfs(node, maxVal):
            if not node:
                return 0  
            
            # Check if current node is "good"
            count_good = 1 if node.val >= maxVal else 0
            
            # Update max value seen so far on the path
            maxVal = max(maxVal, node.val)
            
            # Recur for left and right children
            count_good += dfs(node.left, maxVal)
            count_good += dfs(node.right, maxVal)
            
            return count_good
        
        # Start DFS from root with root's value as initial max
        return dfs(root, root.val)
