#iteration:
def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (not head) or (not head.next):
        return head
    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    
    p1 = self.sortList(slow.next)
    slow.next = None
    p2 = self.sortList(head)
    
    p = res = ListNode(None)
    while p1 and p2:
        if p1.val<p2.val:
            p.next = p1
            p1 = p1.next
            p = p.next
        else:
            p.next = p2
            p2 = p2.next
            p = p.next
    if p1:
        p.next = p1
    if p2:
        p.next = p2
    return res.next

#array...
def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    items = []
    while head:
        items.append(head.val)
        head = head.next
    items.sort()
    p = res = ListNode(None)
    for i in items:
        p.next = ListNode(i)
        p = p.next
    return res.next