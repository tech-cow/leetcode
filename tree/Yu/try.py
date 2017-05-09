def traversal(root):
  if not root:
    return None
  print root.val
  traversal(root.left)
  traversal(root.right)
