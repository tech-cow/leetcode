#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 102. Binary Tree Level Order Traversal

# 思路：
# Recursive，记住Update 一个level的variable，以及设置一个全球，或者local
# （如果local，就必须pass进helper function的parameter）的return array


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(root, level):
            # Edge
            if not root:
                return []
            # Process
            if level >= len(self.res):
                self.res.append([])
            self.res[level].append(root.val)

            # Recursion
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return self.res
