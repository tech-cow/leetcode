#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 515. Find Largest Value in Each Tree Row

# 这道题和打印每一层的数几乎相同（102）
# 本身的思路是原封不动的用102的思路，把所有的数都先Insert到最终的res
# 然后在每个内层的Array取最大值，然后输出，但浪费了太多的空间
# 所以经过改良，每次有新的层数的时候，只需要一个Temp的int值来记录累计最大值就行了
# 节省了很多的空间

# ****************
# Final Solution *
# ****************
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.helper(root, 0)
        return self.res

    def helper(self, node, level):
        if not node:
            return
        if level >= len(self.res):
            self.res.append(node.val)
        self.res[level] = max(self.res[level], node.val)
        self.helper(node.left, level+1)
        self.helper(node.right, level+1)


# ******************
# Before Optimized *
# ******************
class Solution(object):
    def __init__(self):
        self.res = []

    def largestValues(self, root):
        self.helper(root, 0)
        final = []
        for arr in self.res:
            final.append(max(arr))
        return final

    def helper(self, node, level):
        if not node:
            return
        if level >= len(self.res):
            self.res.append([])
        self.res[level].append(node.val)
        self.helper(node.left, level+1)
        self.helper(node.right, level+1)
