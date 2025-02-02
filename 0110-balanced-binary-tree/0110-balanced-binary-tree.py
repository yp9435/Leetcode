# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to perform DFS and check balance
        def dfs(root):
            # Base case: If the node is None (empty subtree), it's balanced with height 0
            if not root:
                return [True, 0]

            # Recursively check left and right subtrees
            left, right = dfs(root.left), dfs(root.right)

            # A tree is balanced if:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. Height difference between left and right subtree is at most 1
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return whether this subtree is balanced and its height (1 + max height of children)
            return [balanced, 1 + max(left[1], right[1])]

        # Start DFS from the root and return whether the entire tree is balanced
        return dfs(root)[0]