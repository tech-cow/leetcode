# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # Edge
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        def findMid(head):
            slow, fast = head, head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            # right here the slow pointer is the mid point
            # ex: when list is 1,2,3,4.  Slow pointer stops @ 3
            # ex2: when list is 1,2,3,4,5    Slow pointer stops @ 3 as well
            pre.next = None
            return slow


        mid = findMid(head)
        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
