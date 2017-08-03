# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
       # Input: The root of a Binary Search Tree like this:
       #        5
       #      /   \
       #     2     13

        self.sum = 0

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val += self.sum
            self.sum = root.val
            dfs(root.left)

        dfs(root)
        return root
