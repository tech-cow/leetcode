#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# ****************

# 思路：
# 首先这题要理解清楚BST的特性
# 左边的数永远比root下，右边的永远比root大
# 所以给你任意两个点，你要找root，若两个点的值都比root小，且两个值都不等于当前的root，则root移动到root.left。
# 同理，相反的话，移至root.right。 直到最后一个比root小，一个比root大，则返回当前root
# 若两个数其中有一个本身就是root，则返回这个数的Node本身。

# ****************
# Final Solution *
# ****************
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        return root
