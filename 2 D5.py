class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    
    def postorder_traversal(self):
        return self._postorder_helper(self.root)
    
    def _postorder_helper(self, node):
        values = []
        if node:
            values += self._postorder_helper(node.left)
            values += self._postorder_helper(node.right)
            values.append(node.value)
        return values

bt = BinaryTree(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)

postorder_values = bt.postorder_traversal()
print(postorder_values)  # Output: [4, 5, 2, 3, 1]