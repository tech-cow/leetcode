# Author: Yu Zhou
# 148. Sort List

# Sort a linked list in O(n log n) time using constant space complexity.

# 思路
# 用链表的方式切分，然后递归Split，之后Merge
# 这道题要注意是切分的时候，要写个Prev的函数用来储存Slow的原点

# Time: O(nlogn)
# Space: O(1)

# ****************
# Final Solution *
# ****************
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        prev = None
        fast = slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev.next = None #截断

        l = self.sortList(head) #递归
        r = self.sortList(mid)
        return self.merge(l, r)


    #这是一种类似于创建一个头的DummyNode，把Head设置成Prev，Cur设置成head.next
    def merge(self, l, r):
        guard = cur = ListNode(None)
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return guard.next

        vhead = curr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return vhead.next


# ***************************************
# The following code is an fail attempt *
# ***************************************
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        fast = slow = head
        #这里错在没有设置一个prev来保存Slow的值
        #每次while结束后，slow就会变成slow.next
        #假如想在slow的地方切断，就必须设置一个Prev
        #来保存slow的值，下方 mid = slow.next
        #其实已经是在经历过while 后的slow.next的next了
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None #截断

        l = self.sortList(head) #递归
        r = self.sortList(mid)
        return self.merge(l, r)
