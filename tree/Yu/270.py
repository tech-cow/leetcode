#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 270. Closest Binary Search Tree Value

# ****************
# Descrption:
# ****************

class Solution(object):
    def closestValue(self, root, target):

        #Edge Case:
        if not root:
            return 0

        self.res = root.val
        #Process
        def dfs(root, target):
            if not root:
                return 0
            if abs(target - self.res) > abs(target - root.val):
                self.res = root.val
            if target > root.val:
                dfs(root.right, target)
            else:
                dfs(root.left, target)

        # Recursion
        dfs(root, target)
        return self.res
