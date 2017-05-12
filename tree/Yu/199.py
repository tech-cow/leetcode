class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Edge
        if not root:
            return []

        self.res = []
        def dfs(root, level):
            # Edge/Condition
            if not root:
                return []
            # Process
            if level == len(self.res):
                self.res.append(root.val)
            # Recursion
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        dfs(root, 0)
        return self.res
