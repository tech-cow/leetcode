# BFS
def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root:
        res,cur = [],[root]
        while cur:
            row,nextr=[],[]
            for i in cur:
                row.append(i.val)
                if i.left: nextr.append(i.left)
                if i.right: nextr.append(i.right) 
            res.append(row)
            cur = nextr
        return res[::-1]
    else:
        return []




# DFS

def dfs(self, node, level, res):
    if node:
        if level > len(res): res.insert(0,[])
        res[-level].append(node.val)
        self.dfs(node.left, level+1, res)
        self.dfs(node.right,level+1, res)
        return res
    

def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    return self.dfs(root,1,[]) if root else []