#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

"""
Recursively compare subtrees
"""


def minDepth(self, root):
    if not root:
        return 0
    left = minDepth(root.left)
    right = minDepth(root.right)
    return left + right + 1 if not left or not right else min(left, right) + 1
