#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# ****************

# 思路：
# 判断括号匹配的合法性。使用一个Stack来解决问题。遇到左括号放入Stack，遇到右括号，检查栈顶的左括号是否匹配
# 如果匹配，pop()，如果不匹配，返回错误。如果栈为空，而遇到右括号，同样返回错误。
# 遍历完后，栈如果不空，同样返回错误，不然过不了 "[" 这种类似的Edge Case
# 这道题也可以用dic来储存左右关系

class Solution(object):
    def isValid(self, s):
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            if char == ')':
                if not stack or stack.pop() != '(':
                    return False
            if char == ']':
                if not stack or stack.pop() != '[':
                    return False
            if char == '}':
                if not stack or stack.pop() != '{':
                    return False
        # Edge for
        # "[" or "{" or "("
        if stack:
            return False
        return True
