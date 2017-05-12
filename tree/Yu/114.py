#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 114 Flatten Binary Tree to Linked List Add to List
# Given a binary tree, flatten it to a linked list in-place.
# ****************

# 思路：
# 对pre-order进行reverse engineering， 每一层递归
# 保存当前节点，用于之后递归时候的拼接

class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #Edge:
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
