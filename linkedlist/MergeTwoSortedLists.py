# Yu Zhou
# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists


#思路
#因为是sorted，只需要设置一个guard_node用来之后的return
#就可以设置一个新的Linkedlist的Node，然后用来储存
#比对完了的值，最后返回guard_node.next(跳过第一个dummy node)就行了

class Solution(object):
    def mergeTwoLists(self, n1, n2):
        #Edge
        if not n1 and not n2:
            return None

        node = guard_node = ListNode(0)

        while n1 and n2:
            if n1.val <= n2.val:
                node.next = n1
                n1 = n1.next
            else:
                node.next = n2
                n2 = n2.next
            node = node.next
        #Edge
        if n1 or n2:
            node.next = n1 or n2

        return guard_node.next
