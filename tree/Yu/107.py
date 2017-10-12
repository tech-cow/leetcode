#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 107. Binary Tree Level Order Traversal II

# 思路：
# 视频参见102，直接把107的res，reverse即可

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(root, level):
            if not root:
                return

            if len(self.res) == level:
                self.res.append([])
            self.res[level].append(root.val)

            left = dfs(root.left, level + 1)
            right = dfs(root.right, level + 1)

        dfs(root, 0)
        return self.res[::-1]
