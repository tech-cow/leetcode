#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 501. Find Mode in Binary Search Tree
# ****************
# Descrption:
# Given a binary search tree (BST) with duplicates, find all the mode(s)
# (the most frequently occurred element) in the given BST.
# ****************

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def find_hash(root, hash):
            # Edge:
            if not root:
                return

            # Process
            if root.val in hash:
                hash[root.val] += 1
            else:
                hash[root.val] = 1

            # Recursion
            find_hash(root.left, hash)
            find_hash(root.right, hash)

        # Edge
        if not root:
            return []

        hash = {}
        res = []
        find_hash(root, hash)

        max_value = max(hash.values())

        for key in hash.keys():
            if hash[key] == max_value:
                res.append(key)
        return res
