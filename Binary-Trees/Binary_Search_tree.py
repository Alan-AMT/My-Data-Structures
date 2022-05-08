class tree_node:
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.root == data:
            raise ValueError("Class 'tree_node' can't have repeated values")
        if data > self.root:
            if self.right:
                self._insert(self.right, data)
            else:
                self.right = tree_node(data)
        else:
            if self.left:
                self._insert(self.left, data)
            else:
                self.left = tree_node(data)

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

    def pre_order(self, sub_tree):
        if sub_tree:
            print(sub_tree.root, end="-")
            self.pre_order(sub_tree.left)
            self.pre_order(sub_tree.right)
            
    def in_order(self, sub_tree):
        if sub_tree:
            self.in_order(sub_tree.left)
            print(sub_tree.root, end="-")
            self.in_order(sub_tree.right)
            
    def post_order(self, sub_tree):
        if sub_tree:
            self.post_order(sub_tree.left)
            self.post_order(sub_tree.right)
            print(sub_tree.root, end="-")

    def __str__(self):
        self.in_order(self)
        return ""
