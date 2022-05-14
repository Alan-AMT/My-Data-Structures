class BinarySearchTree:
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

    def insert(sub_tree, data):
        if sub_tree.root == data:
            raise ValueError("Class 'BinarySearchTree' can't have repeated values")
        if data > sub_tree.root:
            if not sub_tree.right:
                sub_tree.right = BinarySearchTree(data)
            else:
                BinarySearchTree.insert(sub_tree.right,data)
        else:
            if not sub_tree.left:
                sub_tree.left = BinarySearchTree(data)
            else:
                BinarySearchTree.insert(sub_tree.left,data)

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
                print(f"{target} found in BST")
                return None
            if target > sub_tree.root:
                BinarySearchTree.search(sub_tree.right, target)
            else:
                BinarySearchTree.search(sub_tree.left, target)
        else:
            print(f"{target} Not found in BST")
            return None

s = BinarySearchTree(10)
s.insert(11)
s.insert(7)
s.insert(9)
s.insert(56)
s.in_order()
s.search(11)
print()
print(s)
