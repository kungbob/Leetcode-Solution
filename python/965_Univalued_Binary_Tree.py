# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is not None:
            num = root.val
        result = self.loop(root, num)
        return result
    
    def loop(self, root, num):
        if root.val == num:
            result = True
            if root.left is not None:
                result = result and self.loop(root.left, num)
            if root.right is not None:
                result = result and self.loop(root.right, num)
            return result
        else:
            return False