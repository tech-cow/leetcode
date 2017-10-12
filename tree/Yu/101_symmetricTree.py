class Solution(object):
    # Queue
    def isSymmetric(self, root):
        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right,right.left))
        return True        
        
        
    # Recursion
    def isSymmetric2(self, root):
        if not root:
            return True

        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False    
            return dfs(left.left , right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
