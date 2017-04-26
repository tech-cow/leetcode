def helper(self, node, sum, sum_set):
	if node :
    	result = 0
    	#TODO: can be optimize	
    	internal = [i-node.val for i in sum_set]
        result = internal.count(0)
    	internal.append(sum)
    	internal_2 = internal[:]
    	result += self.helper(node.left,sum,internal)
    	result += self.helper(node.right,sum, internal_2)
    	return result
    return 0
	
def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    return self.helper(root,sum,[sum])