#DFS
def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
        if root.left is None and root.right is None:
            return 1
        else:
            l = self.minDepth(root.left) if root.left else sys.maxint
            r = self.minDepth(root.right) if root.right else sys.maxint
            return min(l,r)+1
            
    else:
        return 0

#BFS
def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
        level = 0
        cur = [root]
        while cur:
            level+=1
            nextR = []
            for node in cur:
                if node.left is None and node.right is None:
                    return level
                if node.left: nextR.append(node.left)
                if node.right: nextR.append(node.right)
            cur = nextR
    else:
        return 0