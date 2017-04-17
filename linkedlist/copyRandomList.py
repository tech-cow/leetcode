# 138. Copy List with Random Pointer
# Author: Yu Zhou

# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# 思路：
# 这题其实就是拷贝所有的链表到一个新的
# 唯一的难点是如何在拷贝玩所有链表之后，还能够将Random的指针指对
# 所以这里用的方法是用Hash，然后第一次遍历用来建新的Node
# 第二次遍历用来对Hash里面新建的Node进行指针的赋值

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = dict()
        m = n = head

        #第一次循环用来创建所有原本链表里的Node，并且对他们进行赋值
        #需要搞懂的是，这一次循环，新的链表是一个一个单独的Node，他们的指针都还没有赋值
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next

        #第二次循环，用来对这一个一个独立的Node进行他们的指针赋值，其中包括每个链接下一个Node的指针
        #以及这道题的另一个Random的指针
        while n:
            #这里dic[n].next，dic[n]就是key "n" 相对应的val，也就是之前创建的，RandomListNode(m.label)
            #然后我们对这个新创建的独立Node，设置他的next pointer
            # dic.get(n.next）里面的n.next是reference原List里面的Node的next，不要搞混了
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
