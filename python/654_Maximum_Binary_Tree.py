# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        
        return self.construct(None, nums)
        
    def construct(self, root, nums):
        maxIndex = nums.index(max(nums))
        newNode = TreeNode(nums[maxIndex])
        if maxIndex == len(nums) - 1:
            newNode.right = None
        else:
            rightList = nums[maxIndex +1:]
            newNode.right = self.construct(newNode, rightList)
            
        if maxIndex == 0:
            newNode.left = None
        else:
            leftList = nums[:maxIndex]
            newNode.left = self.construct(newNode, leftList)
        return newNode