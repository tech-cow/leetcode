class Solution(object):
    def maxDistance(self, nums):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        low = float('inf')
        high = float('-inf')
        res = 0
        for num in nums:
            # We can use num[0] && num[-1] only because these lists are sorted
            res = max(res, max(high - num[0], num[-1] - low))
            low = min(low, min(num))
            high = max(high, max(num))
        return res
            
