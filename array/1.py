class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}

        for i , num in enumerate(nums):
            if target - num in dict:
                return (i, dict[target- num])
            else:
                dict[num] = i
