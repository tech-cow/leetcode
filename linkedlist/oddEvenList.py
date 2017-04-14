class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #edge:
        if not head:
            return head

        # Set up runner for odd and even , and a guardnode for return purpose
        odd = head
        even = head.next
        even_guardnode = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_guardnode
        return head

# 思路总结：
# 这题的要求是inplace，所以就用已有的Node进行分配
# 设置一个Odd的runner和一个Even的runner用来遍历
# 一定记住要设置一个Even的guardnode用来返回
# 然后在根据相对的规律遍历完，且建立了新的2组链表关系后
# 将第一个Node，也就是Head，链接到之前保存了的even_guardnode，就把两组链表链接回来了
# 最后返回Head
