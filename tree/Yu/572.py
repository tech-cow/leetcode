#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 572. Subtree of Another Tree

# ****************
# Descrption:
# ****************

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        #Edge
        if not s or not t:
            return False

        #Process
        if self.isMatch(s,t):
            return True

        #Recusion
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        if not s or not t:
            return s == t

        return s.val == t.val and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
