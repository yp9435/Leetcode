# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is None, it is always considered a subtree
        if not subRoot:
            return True
        
        # If root is None but subRoot is not, subRoot can't be a subtree
        if not root:
            return False

        # Check if the current root and subRoot are the same tree using the sameTree function
        if self.sameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees of the root for a match
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # refer Same Tree Leetcode 100
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                   self.sameTree(root.right, subRoot.right))
        return False