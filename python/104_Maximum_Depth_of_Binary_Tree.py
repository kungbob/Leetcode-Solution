# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        depth = self.loop(root, depth)
        return depth
    
    def loop(self, root, depth):
        if root is not None:
            depth += 1
            tempL = depth
            tempR = depth
            if root.left:
                tempL = self.loop(root.left, depth)
            if root.right:
                tempR = self.loop(root.right, depth)
            depth = max([tempL, tempR])
        return depth