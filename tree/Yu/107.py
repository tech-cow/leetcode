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
        res = []
        self.dfs_level(root, 0, res)
        res.reverse()
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
