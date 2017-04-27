# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """a
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        return self.minDepthHelper(root)
    
    def minDepthHelper(self, root):
        
        
        
        if not root:
            return 0
         
        
        if not root.left and not root.right:
            return 1
        
        left = self.minDepthHelper(root.left)
        right = self.minDepthHelper(root.right)
        
        return max(left,right )+1 if left==0 or right==0 else min(left, right)+1
        
        
        
        
    
