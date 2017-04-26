# Preorder traverse, then compare
def left_first(self, root, list):
	if root:
	    list.append(root.val)
	    self.left_first(root.left,list)
	    self.left_first(root.right,list)
	else:
		list.append(None)

def right_first(self,root,list):
	if root:
	    list.append(root.val)
	    self.right_first(root.right,list)
	    self.right_first(root.left,list)
	else:
		list.append(None)

def isSymmetric(self, root):
    if root:
    	list1,list2 = [],[]
    	self.left_first(root.left,list1)
    	self.right_first(root.right, list2)
    	return list1 == list2
    return True


# Traverse each level and compare (BFS)
def isSymmetric(self, root):
    if root:
        left,right = [root.left],[root.right]
        while left and right:
            left_node = left.pop(0)
            right_node = right.pop(0)
            if left_node == None and right_node == None:
                continue
            elif not (left_node and right_node):
                return False
            elif left_node.val != right_node.val:
                return False
            else:
                left.append(left_node.left)
                left.append(left_node.right)
                right.append(right_node.right)
                right.append(right_node.left)
        return True
    return True


#DFS
def dfs(self, left, right):
    if left is None and right is None:
        print "both None"
        return True
    elif not (left and right):
        return False
    else:
        return (left.val == right.val) and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
    
def isSymmetric(self, root):
    if root:
        print "root is not none"
        return self.dfs(root.left, root.right)
    return True
