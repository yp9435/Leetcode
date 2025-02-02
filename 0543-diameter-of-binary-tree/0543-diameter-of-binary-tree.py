# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Variable to store the maximum diameter found
        self.res = 0  

        # to compute height of the tree
        def dfs(root):
            if not root:
                return 0  # Base case: If node is None, height is 0
            
            # Recursively find the height of left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Update the maximum diameter found so far
            # Diameter at this node = left subtree height + right subtree height
            self.res = max(self.res, left + right)

            # Return height of the current node 
            return 1 + max(left, right)

        # Start DFS from the root
        dfs(root)
        
        # Return the maximum diameter found
        return self.res