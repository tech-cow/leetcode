# 582

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """

        hash = {}

        for i, num in enumerate(ppid):
            if num in hash:
                hash[num].append(pid[i])
            else:
                hash[num] = [pid[i]]

        queue = [kill]
        res = []

        while queue:
            parent = queue.pop(0)
            res.append(parent)
            if parent in hash:
                queue += hash[parent]
        return res
