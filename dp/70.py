# 70. Climbing Stairs
# Author: Yu Zhou

# Each time you can either climb 1 or 2 steps.
# 各种方法
# Bottom Up就是从最基本的base case然后慢慢的解决所有的subproblem，指导累计至N
# 这道题因为只Care  N-1 和 N-2 两个值
# 可以直接用O(1)的Space，具体操作就是对两个函数进行更改，而不是存Hash或者Array


# Top Down Recursion (超时)
class Solution(object):
    def climbStairs(self, n):
      # Base case:
      if n == 1:
        return 1
      if n == 2:
        return 2
      return self.climbStairs(n-1) + self.climbStairs(n-2)

# Top Down Memorization DP (Hash表)
class Solution(object):
    def __init__(self):
        self.hash = {1:1, 2:2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.hash:
            self.hash[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.hash[n]

# Bottom-up DP (ArrayList)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        res = [1,2]
        for i in xrange(2, n):
            res.append(res[i-1] + res[i-2])
        return res[-1]

# Bottom-up DP (Constant)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        a, b = 1, 2
        for i in xrange(2, n):
            temp = b
            b = b + a
            a = temp

        return b
