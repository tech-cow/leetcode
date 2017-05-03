# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum=0
            
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        k=[0]
        
        if not root:
            return root
        if root.right:
            self.convertBST(root.right)
        root.val+=self.sum
        self.sum=root.val
        if root.left:
            self.convertBST(root.left)
        return root
            