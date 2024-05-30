# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = collections.defaultdict(int)

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            count[root.val] +=1
            inorder(root.right)
        
        inorder(root)
        mode = max(count.values())
        return [key for key, value in count.items() if value == mode]