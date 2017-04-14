# 143. Reorder List
# Author: Yu Zhou

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# 思路
# 这题的思路是将Node分制
# 设置俩Runner，取中间值，在对中间值后续的Node进行reverse，之后根据顺序合并
# 切记在将一个链表切分的时候，一定要将左边的链表末端指向Null，否则就没切断。

# ****************
# Final Solution *
# ****************
class Solution(object):
    def reorderList(self, head):
        if not head:
            return
        mid = self.findMid(head)
        last_node = self.reverse(mid)
        self.merge(head, last_node)

    def findMid(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        return mid

    def reverse(self, node):
        prev = None
        cur = node

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    # Merge应该设置Next的Guardnode，因为每次我们将Cur Node指向两一个链表的Head Node的时候
    # 我们就缺失原有链表的Next的指针。
    def merge(self, head, end):
        cur1, cur2 = head, end
        while cur2:
            temp1, temp2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1 = temp1
            cur2 = temp2
        return

# ***************************************
# The following code is an fail attempt *
# ***************************************
class Solution(object):
    def reorderList(self, head):
        if not head:
            return
        mid = self.mid_finder(head)
        last_node = self.reverse(mid)
        self.merge(head, last_node)

    def mid_finder(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #这里犯错了，应该把左半边的链表指向Null，不然切不断
            # 缺了slow.next = None
        return slow

    def reverse(self, node):
        prev = None
        cur = node
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def merge(self, head, last):

        first = head
        while last:
           first.next = last
           first = first.next
           last.next = first
           last = last.next
        return
