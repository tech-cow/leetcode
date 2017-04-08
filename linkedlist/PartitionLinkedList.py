# Definition for singly-linked list.
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


#思路
#设置两个guardnode
#然后制造两个temp node用于循环
#将第一个链表的末尾指向第二个的开头，返还第一个guardnode.next

class Solution(object):
    def partition(self, head, x):
        small, large = ListNode(0), ListNode(0)
        cur1, cur2 = small, large

        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next

            head = head.next

        cur2.next = None
        cur1.next = large.next

        return small.next
