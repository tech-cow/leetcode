# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = fast = head
        for _ in xrange(n):
            fast = fast.next

        # 我本来的代码没有15-16行，可以给我解释下这个edge case干了什么么
        # 论坛里面都设置了dummynode，这题为什么要设置dummynode
        # 先去玩狼人杀，回来继续研究
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
