# Yu Zhou
# 78. Subsets
# Given a set of distinct integers, nums, return all possible subsets.
# Note: The solution set must not contain duplicate subsets.

# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(nums, temp, i):
            self.res.append(temp[:])
            for i in xrange(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()
        dfs(nums, [], 0)
        return self.res
