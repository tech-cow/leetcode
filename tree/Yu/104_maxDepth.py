#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# Given a binary tree, find its maximum depth.
# ****************

# 思路：
# 基础题，确保有Root就行。然后递归

# ****************
# Final Solution *
# ****************
class Solution(object):
    def maxDepth(self, root):
      if not root:
          return 0
      else:
          return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        
# ********************
# Divide and Conquer *
# ********************        
class Solution(object):
    def maxDepth(self, root):
         
        if not root:
            return 0
        else:
            # using Divide and Conquer
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1
