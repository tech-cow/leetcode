# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, num, path, res):
        left = num - node.val
        if left == 0 and (not node.left) and (not node.right):
            res.append(path+[node.val])
        elif (not node.left) and (not node.right):
            return
        else:
            if node.left: self.helper(node.left, left, path+[node.val],res)
            if node.right: self.helper(node.right, left, path+[node.val], res)
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        path,res = [],[]
        self.helper(root, sum, path, res)
        return res

        