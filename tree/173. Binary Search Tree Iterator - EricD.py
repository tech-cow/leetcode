# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.list = []
        self.inOrder(root)
        self.i = 0
        
    def inOrder(self,node):
        if not node:
            return
        self.inOrder(node.left)
        self.list.append(node.val)
        self.inOrder(node.right)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.list)
        

    def next(self):
        """
        :rtype: int
        """
        self.i+=1
        return self.list[self.i-1]
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())