#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 111. Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.
# ****************

# 思路：
# 思考四种Case
# 1. 有或者没有Root
# 2. 有root.left，没有root.right
# 3. 有root.right, 没有 root.left
# 4. 两个Children都有

# ****************
# Final Solution *
# ****************
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right))+ 1


# 底下这个方法其实更好理解，Final的方法刚开始看别人写没看懂，是底下这种方法的改良
# ***************
# Older Version *
# ***************
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+ 1
