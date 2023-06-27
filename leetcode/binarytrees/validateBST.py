# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True
            elif left >= node.val or right <= node.val:
                return False
            else:
                return validate(node.left, left, node.val) and validate(node.right, node.val, right)
        return validate(root, float("-inf"), float("inf"))