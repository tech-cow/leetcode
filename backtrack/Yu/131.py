#131. Palindrome Partitioning


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, temp):
        if not s:
            self.res.append(temp[:])
            return

        for i in xrange(1,len(s)+1):
            if self.isPali(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:], temp)
                temp.pop()


    def isPali(self, s):
        return s == s[::-1]
