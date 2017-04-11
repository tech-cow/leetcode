class Solution(object):
    def removeElements(self, head, target):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #Get rid of the first replica
        while head and head.val == target:
            head = head.next


        cur = head
        while cur:
            if cur.next and cur.next.val == target:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
