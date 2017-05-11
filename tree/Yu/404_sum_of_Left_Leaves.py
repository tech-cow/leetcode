class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Edge
        if not root:
            return 0
        # Process
        self.count = 0
        def dfs(root):
            if not root:
                return 0
            if root.left and not root.left.left and not root.left.right:
                self.count += root.left.val
            # Recursion
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.count
