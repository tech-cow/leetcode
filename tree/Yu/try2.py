# '''
#     1
#   /   \
#  2      3
# / \     / \
# 1  3   6   2
#             \
#              5
#
#              1
#            /   \
#           3      2
#          / \     / \
#         2   6   3   1
#        /
#       5

def inverseTree(root):
  # if root.left or root.right:
  temp = root.left
  root.left = root.right
  root.right = temp


#
# return 3
#
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
#
# return 2
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#   2
#  / \
# 0   5
#
# '''
#
#
#
#
# def longestCon(root):
#     '''
#     input: TreeNode
#     output: int
#     '''
#     def dfs_level(node, max_num):
#         if not root:
#             return 0
#         cur = 1
#         left = dfs_level(node.left)
#         right = dfs_level(node.right)
#
#         if node.left:
#             if node.val + 1 == node.left.val:
#                 cur = max(cur, left + 1)
#         if node.right:
#             if node.val + 1 == node.right.val:
#                 cur = max(cur, right + 1)
#         max_num = max(max_num, cur)
#         return cur
#
#     max_num = 0
#     dfs_level(root, max_num)
#     return max_num
