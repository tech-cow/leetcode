class Solution(object):
    # DFS Recursion
    def averageOfLevels(self, root):
        self.res = []

        def dfs(root, level):
            if not root:
                return []
            if len(self.res) == level:
                self.res.append([])
            self.res[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return [sum(num)/float(len(num)) for num in self.res]

    # DFS Recursion, Optimized using Tuples
    def averageOfLevels2(self, root):
        self.res = []

        def dfs(root, level):
            if not root:
                return []
            if len(self.res) == level:
                self.res.append([0,0])
            self.res[level][0] += root.val
            self.res[level][1] += 1.0
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return [num/count for num, count in self.res]
