# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        tempSum = 0
        result = self.dfs(root, sum, tempSum)
        return result
        
    def dfs(self, root, sum, tempSum):
        tempSum += root.val
        if root.left is None and root.right is None:
            if tempSum == sum:
                return True
            else:
                return False
        
        resultL = False
        resultR = False
        if root.left is not None:
            resultL = self.dfs(root.left, sum, tempSum)
            
        if root.right is not None:
            resultR = self.dfs(root.right, sum, tempSum)
            
        return resultR or resultL