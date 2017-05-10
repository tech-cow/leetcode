#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 257. Binary Tree Paths

# 思路：
# DFS + Stack

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = [(root, "")]
        res = []

        # Edge Case
        if not root:
            return []

        # res: ["1->3", "1->2->5"]
        while stack:
            node, strr = stack.pop()
            if not node.left and not node.right:
                res.append(strr + str(node.val))
            if node.left:
                stack.append((node.left, strr + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, strr + str(node.val) + "->"))
        return res


# Recursive DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        #Edge
        if not root:
            return []
        self.dfs(root, "")
        return self.res

    def dfs(self, root, strr):
        if not root.left and not root.right:
            self.res.append(strr + str(root.val))
        if root.left:
            self.dfs(root.left, strr + str(root.val) + "->")
        if root.right:
            self.dfs(root.right, strr + str(root.val) + "->")
