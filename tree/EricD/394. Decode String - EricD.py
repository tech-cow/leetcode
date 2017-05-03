class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                word = []
                while stack[-1] != '[':
                    word.append(stack.pop())
                stack.pop()
                freq = []
                while stack and stack[-1].isdigit():
                    freq.append(stack.pop())
                k=''.join(freq[::-1])
                w  = ''.join(word[::-1])
                stack.append(w*int(k))
            
        return ''.join(stack)
            