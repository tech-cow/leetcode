def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    stack = []
    while root:
    	stack.append(root)
    	root = root.left
    
    while stack:
    	tmp = stack.pop()
    	res.append(tmp.val)
    	if tmp.right:
    		t = tmp.right
    		#add all left
    		while t:
    			stack.append(t)
    			t = t.left
    return res