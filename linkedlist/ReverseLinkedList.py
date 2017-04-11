class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None

        while cur:
            #设置一个next用来保存之后所有的链表链接，否则改了cur.next以后，
            #第一个node就和之后的链表失联了
            next = cur.next
            #将cur的指针指向prev，也就是Null
            cur.next = prev
            #跟换prev的reference到cur，然后之后可以通过指针reference到这个prev
            #的Node
            prev = cur
            #跟换cur到next,也就是之前为防止数据丢失而保存的reference
            cur = next
        #当list遍历到最后，把头reference到最后面一个node
        head = prev
        return head
