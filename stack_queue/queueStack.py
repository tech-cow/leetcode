#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 225. Implement Stack using Queues
# ****************

# 思路：
# pop方程的思路：
# 在每次pop的时候，将整个queue移动一遍。这里注意的是，移动Length - 1次就够了
# 因为在我们最终还是Pop掉stack最后一个值，也就是在移动Length - 1次以后的第一个值

# top方程的思路：
# 和pop接近，这里注意的是，在进行一次完整的换位，在最后一次换位前，记得把temp保存下来
# 用于之后返回
# 例如 [3,4,5]， 进过一次遍历： [4,5,3]   两次： [5,3,4]
# 这个时候要保存5,因为5是top value，再将Queue变回原来的 [3,4,5]


# ****************
# Final Solution *
# ****************
class MyStack(object):
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.queue:
            for _ in xrange(len(self.queue) - 1):
              self.queue.append(self.queue.pop(0))
            return self.queue.pop(0)
        else: return []

    def top(self):
        temp = 0
        for _ in xrange(len(self.queue)):
            temp = self.queue.pop(0)
            self.queue.append(temp)
        return temp

    def empty(self):
        return False if self.queue else True
