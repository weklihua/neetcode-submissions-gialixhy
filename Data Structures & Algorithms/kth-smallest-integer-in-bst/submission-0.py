# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def traverse(node):

            if not node:
                return
            
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
            return res

       
        result = traverse(root)
        
        return result[k - 1]

        