#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:

# Time:  O(n)
# Space: O(1)
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA)
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).”
#
#         _______6______
#       /              \
#     ___2__          ___8__
#   /      \        /      \
#   0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2, since a node can be a
# descendant of itself according to the LCA definition.

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
    #Iterative
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return None

        while root:
            if root.val > max(p.val, q.val):
                root = root.left
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                return root


    #Recursion
    def lowestCommonAncestor2(self, root, p, q):
        if not root or not p or not q:
            return None
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
