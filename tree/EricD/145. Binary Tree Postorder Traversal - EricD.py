def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res,stack = [],[]
    while root:
        res.append(root.val)
        stack.append(root)
        root = root.right
    while stack:
        tmp = stack.pop()
        if tmp.left:
            t = tmp.left
            while t:
                res.append(t.val)
                stack.append(t)
                t = t.right
    return res[::-1]