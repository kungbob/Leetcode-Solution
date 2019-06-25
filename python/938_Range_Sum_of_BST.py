# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = self.calculate(root, L, R, 0)
        return result
    
    def calculate(self, root, L, R, temp):
        test = temp
        if root.left is not None:
            temp += self.calculate(root.left, L, R, test)
            
        if root.right is not None:
            temp += self.calculate(root.right, L, R, test)
            
        if root.val >= L and root.val <= R:
            temp += root.val
        
        return temp