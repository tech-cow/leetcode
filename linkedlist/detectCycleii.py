class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        while head != slow:
            head = head.next
            slow = slow.next
        return head

# 大致思路
# 这道题不是那种一看就能知道做法的
# 大致意思是当Fast和Slow重合的时候，他们离开起始Loop的距离
# 和Head离开Loop起始的距离是相等的
# 所以有了以上代码的形式。

# 另外一种解法
# 可以用一个Set来储存遍历过得Node，然后若发现有重复
# 返回那个重复的点。 不过这个需要 O（N）的空间
# 违背了题目的要求。
