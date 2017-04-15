# Author: Yu Zhou
# 61. Rotate List

# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Time: O(n)
# Space: O(1)

# 思路
# 先Pad距离，然后用Mod测量周期，最后将之前切断的两节链表链接起来

# ****************
# Final Solution *
# ****************
class Solution(object):
    def rotateRight(self, head, k):
        #Edge
        if not head or not head.next:
            return head

        cur, count = head, 0

        #Count Length for modular operation
        while cur:
            cur = cur.next
            count += 1
        mod = k % count

        #Edge2
        if k == 0 or mod == 0:
            return head

        slow = fast = head
        for _ in xrange(mod):
            fast = fast.next

        # Use fast.next here so fast point doesn't reach Null
        while fast.next:
            slow = slow.next
            fast = fast.next

        newHead = slow.next
        fast.next = head
        slow.next = None

        return newHead

# ***************************************
# The following code is an fail attempt *
# ***************************************
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None

        slow = fast = head

        for _ in xrange(k):
            fast = fast.next

        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = None
        newHead = cur = slow

        while cur.next:
            cur = cur.next

        cur.next = head
        return newHead
