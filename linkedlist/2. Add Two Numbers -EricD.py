def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l3 = res = ListNode(None)
    p=0
    while l1 and l2:
        n,p = (l1.val+l2.val+p)%10,(l1.val+l2.val+p)/10
        l3.next = ListNode(n)
        l3 = l3.next
        l1 = l1.next
        l2 = l2.next
    while l1:
        n,p = (l1.val+p)%10,(l1.val+p)/10
        l3.next = ListNode(n)
        l3 = l3.next
        l1 = l1.next
    while l2:
        n,p = (l2.val+p)%10,(l2.val+p)/10
        l3.next = ListNode(n)
        l3 = l3.next
        l2 = l2.next
    if p>0:
        l3.next = ListNode(p)
    return res.next