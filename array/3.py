class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Edge
        if not s:
            return 0

        start, max_length, hash = 0, 0, {}

        for i, num in enumerate(s):
            # Need to have the following condition:
            # start <= hash[num] to avoid edge case such as :
            # "tmmzuxt"
            if num in hash and start <= hash[num]:
                #update pointer
                start = hash[num] + 1
            else:
                max_length = max(max_length, i - start + 1)

            hash[num] = i

        return max_length
