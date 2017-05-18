#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 47. Combinations
# 多了个condition用来去重，其他一样
# 哦，还有就是不能有相同当前的值
# 所以index传递是i + 1
# 因为要去重，所以我们要先排序，比对关系是前后比对。


class Solution(object):
    def combinationSum2(self, nums, target):
        self.res = []
        def dfs(nums,temp,index, remainder):
            if remainder == 0:
                self.res.append(temp[:])
                return

            if remainder < 0:
                return

            for i in range(index, len(nums)):
                if i>index and nums[i] == nums[i-1]: continue
                temp.append(nums[i])
                dfs(nums, temp, i + 1, remainder - nums[i])
                temp.pop()

        dfs(sorted(nums),[], 0, target)
        return self.res
