# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
            
        elif root.left is None and root.right is None:
            return 1
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
