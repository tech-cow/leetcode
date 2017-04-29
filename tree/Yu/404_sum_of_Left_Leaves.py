class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if root.left and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)

        return left + right
