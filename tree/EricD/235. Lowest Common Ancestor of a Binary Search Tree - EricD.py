# Binary Search Tree! 
def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    while (root.val-p.val)*(root.val-q.val)>0:
        root = root.left if root.val>q.val else root.right
    return root