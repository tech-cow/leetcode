#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# ****************
# Final Solution *
# ****************
class Solution(object):
    def addTwoNumbers(self, n1, n2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        temp = ret
        carry = 0
        while n1 or n2 or carry:
            result = carry
            if n1:
                result += n1.val
                n1 = n1.next
            if n2:
                result += n2.val
                n2 = n2.next
            newNode = ListNode(result % 10)
            carry = result / 10
            temp.next = newNode
            temp = temp.next
        return ret.next


# ***************************************
# The following code is an fail attempt *
# ***************************************

class Solution(object):
    def addTwoNumbers(self, n1, n2):
        ret = ListNode(0)
        temp = ret
        carry = 0
        while n1 or n2:
            result = carry

            if n1:
                result += n1.val
                n1 = n1.next
            if n2:
                result += n2.val
                n2 = n2.next
            newNode = ListNode(result % 10)
            carry = result / 10
            print newNode.val
            temp.next = newNode
        return ret.next

# 代码解析：
# 首先代码打印不出来，因为忘记了一个重要的步骤
# 当把Temp.next指向newNode以后，我没有更新Temp本身，所以，temp永远处于
# ret的位置，所以应该是
#       temp.next = newNode
#       temp = temp.next

# 然后代码还是不工作，因为忘记了一个Edge case
# 当这段代码运行至  n1或者n2的底端，自动就结束了
# 若是最后两个数相加有一个carry，就会被Truncate掉
# 所以应该在while里面加一个condition
#       while n1 or n2 or carry:
