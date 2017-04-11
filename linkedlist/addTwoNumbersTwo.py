#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# ****************
# Final Solution *
# Using Stack    *
# ****************
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, n1, n2):
       l1 = self.list_to_stack(n1)
       l2 = self.list_to_stack(n2)
       stack = self.add_helper(l1,l2)
       return self.stack_to_list(stack)

    def list_to_stack(self, node):
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        return stack

    def add_helper(self, s1, s2):
        res = []
        carry = 0
        while s1 or s2 or carry:
            num1 = s1.pop() if s1 else 0
            num2 = s2.pop() if s2 else 0
            total = num1 + num2 + carry
            res.append(total % 10)
            carry = total/10
        return res

    def stack_to_list(self, stack):
        head = ListNode(0)
        cur = head
        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next
        return head.next


# *****************************************
# The following code is an fail attempt   *
# Passed 893/1539 Test Cases              *
# Failed Cases such as 1 + 99(Getting 01) *
# *****************************************
class Solution(object):
    def addTwoNumbers(self, n1, n2):
        #Pad The Two List
        len1, len2 = self.get_length(n1), self.get_length(n2)
        if len1 > len2:
            #Insert Dummy Node to head
            for _ in range(len1-len2):
                temp = ListNode(0)
                temp.next = n2
                n2 = temp
        else:
            for _ in range(len2-len1):
                temp = ListNode(0)
                temp.next = n1
                n1 = temp

        has_carry_head = False
        #Edge: Largest Carry
        res = cur = ListNode(0)
        guard1, guard2 = n1, n2
        carry = 0
        while n1 or n2 or carry:
            if n1.next and n2.next:
                carry = (n1.next.val + n2.next.val) / 10
            result = carry + n1.val + n2.val
            temp = ListNode(result % 10)
            front_carry = result / 10
            cur.next = temp
            cur = cur.next

            n1 = n1.next
            n2 = n2.next

        if guard1.val + guard2.val + front_carry > 10:
            res.val = 1
            has_carry_head = True

        print has_carry_head
        return res if has_carry_head else res.next

    def display(self,node):
        cur = node
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print arr

    def get_length(self, node):
        cur = node
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

#失败心经
# 讲道理，现在还是懵的。。首先insert方程和pad方程
# 若是单独写一个方程，然后带入，不知道为什么不能pass by reference
# 所以后来很机械化的没有写进方程
# 这个代码大部分的Test Case都能过，有一些小的，是在不知道怎么调了
# 因为弄得特别的乱，大概思路就是Pad两个List，然后加减，CC189的套路
# 这道题后来看了答案，可以用Stack来写。
