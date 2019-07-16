"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        result = self.loop(root, result)
        return result
        
    def loop(self, root, result):
        if root is not None:
            result.append(root.val)
            for child in root.children:
                result = self.loop(child, result)
        return result