#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

"""
Recursively compare subtrees
"""

def is_symmetric(self, root):
    return not root or symmetric(root.left, root.right)


def symmetric(node1, node2):
    # Using try catch follows python EAFP coding style
    try:
        return node1.val == node2.val and symmetric(node1.left, node2.right) and symmetric(
            node1.right, node2.left)
    except:
        return node1 is node2
