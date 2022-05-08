class tree_node:
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.right and data > self.root:
            self._insert(self.right, data)
        elif self.left and data < self.root:
            self._insert(self.left, data)
        elif not self.left and data < self.root:
            self.left = tree_node(data)
        elif not self.right and data > self.root:
            self.right = tree_node(data)

    @staticmethod
    def _insert(sub_tree, data):
        if sub_tree.root == data:
            raise ValueError("Class 'tree_node' can't have repeated values")
        if data > sub_tree.root:
            if not sub_tree.right:
                sub_tree.right = tree_node(data)
            else:
                sub_tree._insert(sub_tree.right, data)
        else:
            if not sub_tree.left:
                sub_tree.left = tree_node(data)
            else:
                sub_tree._insert(sub_tree.left, data)
