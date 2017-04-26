def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
    else:
        return 0