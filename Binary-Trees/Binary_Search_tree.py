from Binary_Tree import BinaryTree

class BinarySearchTree(BinaryTree):
    def __init__(self, data):
        super().__init__(data)
        
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
print(s.in_order())
