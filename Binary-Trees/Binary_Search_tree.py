class BinarySearchTree:
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
                self.right = BinarySearchTree(data)
        else:
            if self.left:
                self._insert(self.left, data)
            else:
                self.left = BinarySearchTree(data)

    @staticmethod
    def _insert(sub_tree, data):
        if sub_tree.root == data:
            raise ValueError("Class 'tree_node' can't have repeated values")
        if data > sub_tree.root:
            if not sub_tree.right:
                sub_tree.right = BinarySearchTree(data)
            else:
                sub_tree._insert(sub_tree.right, data)
        else:
            if not sub_tree.left:
                sub_tree.left = BinarySearchTree(data)
            else:
                sub_tree._insert(sub_tree.left, data)

    def pre_order(sub_tree):
        if sub_tree:
            print(sub_tree.root, end="-")
            BinarySearchTree.pre_order(sub_tree.left)
            BinarySearchTree.pre_order(sub_tree.right)
            
    def in_order(sub_tree):
        if sub_tree:
            BinarySearchTree.in_order(sub_tree.left)
            print(sub_tree.root, end="-")
            BinarySearchTree.in_order(sub_tree.right)
            
    def post_order(sub_tree):
        if sub_tree:
            BinarySearchTree.post_order(sub_tree.left)
            BinarySearchTree.post_order(sub_tree.right)
            print(sub_tree.root, end="-")

    def __str__(self):
        self.in_order()
        return ""

    def search(sub_tree, target):
        if sub_tree:
            if sub_tree.root == target:
                print("found")
                return None
            if target > sub_tree.root:
                BinarySearchTree.search(sub_tree.right, target)
            else:
                BinarySearchTree.search(sub_tree.left, target)
        else:
            print("nel")
            return None
        
# ------------- TEST ---------------- #
t = BinarySearchTree(10)
t.insert(7)
t.insert(6)
t.insert(8)
t.insert(1)
t.insert(9)
t.insert(11)
t.insert(20)
t.insert(14)
t.insert(22)
BinarySearchTree.pre_order(t)
print()
BinarySearchTree.in_order(t)
print()
BinarySearchTree.post_order(t)
print()
print(t)
BinarySearchTree.search(t,14)
