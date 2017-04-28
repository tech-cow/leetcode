# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        return self.isSameTreeHelper(p, q)
        
    def isSameTreeHelper(self, p, q):
        
        if not p and not q:
            return True
            
        if (not p and q) or (not q and p):
            return False
        
        
        return p.val==q.val and self.isSameTreeHelper(p.left, q.left) and self.isSameTreeHelper(p.right, q.right)
