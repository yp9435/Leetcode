# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty, they are the same (both None)
        if not p and not q:
            return True
        
        # If one of the trees is empty or the values at the current nodes don't match, return False
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check if the left subtrees and right subtrees are the same
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
