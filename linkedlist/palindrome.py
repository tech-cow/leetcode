# 234. Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.
# Time: O(n)
# Space: O(1)

# 思路：
# 设置快慢pointer，当快的pointer指向最后的时候，慢的正好是中间
# 以中间的Node为起始，开始reverse后半边的链表
# 从Head和Tail开始往中间循环，比对

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        #Reverse here
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        tail = prev

        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
