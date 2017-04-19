#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# 155. Min Stack
# Time: O(1)
# Space: O(n)  using extra stack

# Descrption:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# ****************

# 思路：
# 创建一个额外的stack用来储存所有的最小值
# 返回Min的时候，就返回minstack的最后一个值就好了


# ****************
# Final Solution *
# ****************
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)
        if self.minstack:
            x = min(self.minstack[-1], x)
        self.minstack.append(x)

    def pop(self):
        self.minstack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]
