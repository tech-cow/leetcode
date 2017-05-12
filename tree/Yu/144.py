#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# 144. Binary Tree Preorder Traversal
# Descrption:
# Given a binary tree, return the preorder traversal of its nodes' values.
# ****************
# Time Complexity O(N) | Space O(N)

# Stack/ Iterative
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

# DFS/ Recursive
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root, res):
            if root:
                res.append(root.val)
                dfs(root.left, res)
                dfs(root.right, res)
            return res
        return dfs(root,res)
