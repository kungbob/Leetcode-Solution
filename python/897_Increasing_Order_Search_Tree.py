# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        array = []
        array = self.loop(root, array)
        if len(array) == 0:
            return None
        head = TreeNode(array[0])
        current = head
        for i in range(1, len(array)):
            current.right = TreeNode(array[i])
            current.left = None
            current = current.right
        return head
        
    def loop(self, root, array):
        if root is not None:
            if root.left is not None:
                self.loop(root.left, array)
            array.append(root.val)
            if root.right is not None:
                self.loop(root.right, array)
        return array
        