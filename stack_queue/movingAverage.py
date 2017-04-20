#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 346. Moving Average from Data Stream

#Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# ****************

# 思路：
# 没什么难度，基础的stack知识，当size超过self.size的时候，pop掉第一个进入queue的，再加上新的就行了
# 若没超过size，就继续push

# ****************
# Final Solution *
# ****************
class MovingAverage(object):
    def __init__(self, size):
        self.size = size
        self.queue = []

    def next(self, val):
        if not self.queue or len(self.queue) < self.size:
            self.queue.append(val)
        else:
            self.queue.pop(0)
            self.queue.append(val)
        return float(sum(self.queue)) / len(self.queue)
