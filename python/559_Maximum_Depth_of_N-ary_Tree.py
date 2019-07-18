"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        result = 0
        result = self.loop(root, result)
        return result
        
    def loop(self, root, depth):
        while root is not None:
            depth += 1
            if len(root.children) == 0:
                return depth
            else:
                maxN = depth
                for child in root.children:
                    temp = self.loop(child, depth)
                    if temp > maxN:
                        maxN = temp
                return maxN
        return depth