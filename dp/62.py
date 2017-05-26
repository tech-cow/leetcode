class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #edge:
        if not m or not n:
            return 0

        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
