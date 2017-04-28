# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return root
        
        maxval = max(p.val, q.val)
        minval = min(p.val, q.val)
        
        while root:
            
            if minval<=root.val<=maxval:
                return root
                
            elif root.val>maxval:
                root = root.left
            
            elif root.val<minval:
                root = root.right
                
            
        
        return root
          
        
