# 24. Swap Nodes in Pairs
# Author: Yu Zhou

# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# 思路

# 这题的关键是处理每个Node的指针关系
# 设置3个pointer， p0也就是prev，p1是head, p2是next
# 然后把关系通过纸画下来，就能够理解个个pointer的关系了。
# 之前我的想法特别奇葩，在下面的代码里，感觉也没写对。。

# ****************
# Final Solution *
# ****************
class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head

        guard = p0 = ListNode(0)
        guard.next = head

        while p0.next and p0.next.next:
            p1 = p0.next  #第一个交换数
            p2 = p0.next.next  #第2个交换数

            p0.next = p2
            p1.next = p2.next
            p2.next = p1

            p0 = p0.next.next

        return guard.next

# ***************************************
# The following code is an fail attempt *
# ***************************************
class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head

        dummy1 , dummy2 = ListNode(0), ListNode(0)

        cur = head.next
        while cur:
            dummy1.next = cur
            if cur.next:
                cur = cur.next.next

        cur = head
        while cur and cur.next:
            dumm2.next = cur
            cur = cur.next.next

        #merge
        dummy = ListNode(0)
        dummy.next = head
        while dummy1 and dummy2:
            dummy.next = dummy1
            dummy = dummy.next
            dummy1 = dummy1.next

            dummy.next = dummy2
            dummy = dummy.next
            dummy2 = dummy2.next

        if dummy1:
            dummy.next = dummy1
        if dummy2:
            dummy.next = dummy2

        return dummy.next
