def helper(self,node,res):
    if not node:
        return 0
    l = self.helper(node.left,res)
    r = self.helper(node.right,res)
    res[0] = max(res[0],l+r)
    return 1+max(l,r)

def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    res = [0]
    self.helper(root,res)
    return res[0]