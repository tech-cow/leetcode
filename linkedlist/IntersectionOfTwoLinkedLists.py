class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        #Count the length for both listnode
        curA ,curB = headA ,headB
        len_a = self.lengthcount(curA)
        len_b = self.lengthcount(curB)

        # Reset pointer, because they both pointers point to the end already.....
        curA ,curB = headA ,headB

        #pad
        if len_a > len_b:
            for _ in xrange(len_a - len_b):
                curA = curA.next
        elif len_b > len_a:
            for _ in xrange(len_b - len_a):
                curB = curB.next

        while curA != curB:
            curA = curA.next
            curB = curB.next

        return curA

    def lengthcount(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
