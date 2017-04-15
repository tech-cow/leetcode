# Author: Yu Zhou
# 83. Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# 思路，不需要删除这个Node，只需要将Pointer指向之后的一个Node就行
# 中间有个容易出错的就是，不要每次While循环，自动位移当前的Pointer
# 在比对完当前Node和后面的所有Node直到没有重复的时候
# 再 cur = cur.next

# ****************
# Final Solution *
# ****************
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# ***************************************
# The following code is an fail attempt *
# ***************************************
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
        #问题出在这里
        #cur不应该在每次比对以后直接位移，应该等没有
        #duplicate以后再位移，所以这里要加Else
        #不加的后果是，底下之中corner case会失败: [1,1,1]
            cur = cur.next
        return head
