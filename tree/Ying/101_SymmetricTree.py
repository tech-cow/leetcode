# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        
        if not root:
            return True
        
        return self.compareTree(root.left, root.right)
        
        
    
    def compareTree(self, left, right):
        
        if not left and not right:
            return True
            
        
    
        
        if (not left and right) or  (not right and left):
            return False
        
            
        
            
        return left.val==right.val and self.compareTree(left.left, right.right) and self.compareTree(left.right, right.left)
        
        
        
    
