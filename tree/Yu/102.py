#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 102. Binary Tree Level Order Traversal

# 思路：
# Recursive，记住Update 一个level的variable，以及设置一个全球，或者local
# （如果local，就必须pass进helper function的parameter）的return array


class Solution(object):
    #def __init__(self):
     #   self.res = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs_level(root, 0, res)
        return res

    def dfs_level(self, node, level, res):
        #Edge
        if not node:
            return
        #res: [[3],[9, 20], [15,7 ]]
        if level >= len(res):
            res.append([])
        res[level].append(node.val)
        self.dfs_level(node.left, level+1, res)
        self.dfs_level(node.right, level+1, res)
