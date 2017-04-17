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

        # 总算懂这个Cornor Case了
        # 因为没有设置DummyNode，如果出现以下的这个Cornor Case
        # 1 -> 2， 然后 N = 2
        # 我们要做什么呢，删除1，然后返回2，也就是size of the list
        # 但如何删除1，也就是Head，以下所有的代码都没有考虑到这个点
        # 如果有个DummyHead，我们可以尽管的将DummyHead连接到Head，
        # 然后将DummyHead指到2就行了，Head就删除了
        # 若没有DummyHead，以下的代码无法处理Head被删除的Cornor Case

        # 那么这个Cornor case就牛逼了
        # 在没有Cornor Case的情况下，if not fast，也就意味着size就等于N
        # 直接返回head.next，也就意味着删除了Head，牛不牛！？
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
