#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 226. Invert Binary Tree

# ****************
# Descrption:
# Invert a binary tree
# ****************

# 思路：
# 每层需要进行左右的互换
# 完了以后向上返回就行


# ****************
# Final Solution *
# ****************
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        #Edge
        if not root:
            return

        #Swap
        temp = root.left
        root.left = root.right
        root.right = temp

        #Recusion
        self.invertTree(root.left)
        self.invertTree(root.right)

        #Return
        return root
