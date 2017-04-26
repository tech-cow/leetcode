#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

"""
Recursively compare subtrees
"""

def isSameTree(p, q):
    #EAFP
    try:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    except:
        return p is q
