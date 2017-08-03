# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isMatch(s, t):
            # 在每层的当前节点，做一套整体的比较
            # Edge
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val == t.val:
                return isMatch(s.left, t.left) and isMatch(s.right, t.right)
            else:
                return False

        if isMatch(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
