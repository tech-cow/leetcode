#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# Given two binary trees, write a function to check if they are equal or not.
# ****************
# Time Complexity O(N) | Space O(N)


# Recursive思路：
# 解决EdgeCase以后
# 在默认p和q是同一个节点的情况下，先比对当前层次的val，然后递归往下再进行对比
# 因为遍历了整个树，所以空间和时间都是O（N）

# ****************
# Final Solution *
#   Recursive    *
# ****************
class Solution(object):
    def isSameTree(self, p, q):
        #Edge
        if not p or not q:
            return p == q
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# ***************
# Older Version *
# ***************
def isSameTree(self, p, q):
        #Edge
        if not p or not q:
            return p == q
        #Root Case
        elif p.val != q.val:
            return False
        #The rest
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
