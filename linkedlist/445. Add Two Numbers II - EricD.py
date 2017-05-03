def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n1,n2=0,0
    while l1:
        n1 = n1*10+l1.val
        l1 = l1.next
    while l2:
        n2 = n2*10+l2.val
        l2 = l2.next
    
    sum = str(n1+n2)
    cur = res = ListNode(None)
    for n in sum:
        cur.next =ListNode(n)
        cur = cur.next
    return res.next