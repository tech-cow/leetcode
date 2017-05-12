#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 230. Kth Smallest Element in a BST
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# ****************

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = 0

        def dfs(root):
            # Edge/Condition
            if not root:
                return 0

            dfs(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.right)

        dfs(root)
        return self.res
