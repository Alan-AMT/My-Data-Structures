from Binary_Tree_Interface import BinaryTreeInterface

class BinaryTree(BinaryTreeInterface):
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None
    
    #Traversal functions are meant to return a list with all the roots of the tree
    #pre/in/post_order_list is an optional parameter if you want to append the roots to a specific list
    def pre_order(sub_tree, pre_order_list = []):
        if sub_tree:
            pre_order_list.append(sub_tree.root)
            BinarySearchTree.pre_order(sub_tree.left)
            BinarySearchTree.pre_order(sub_tree.right)
        return pre_order_list
            
    def in_order(sub_tree, in_order_list = []):
        if sub_tree:
            BinarySearchTree.in_order(sub_tree.left)
            in_order_list.append(sub_tree.root)
            BinarySearchTree.in_order(sub_tree.right)
        return in_order_list
            
    def post_order(sub_tree, post_order_list = []):
        if sub_tree:
            BinarySearchTree.post_order(sub_tree.left)
            BinarySearchTree.post_order(sub_tree.right)
            post_order_list.append(sub_tree.root)
        return post_order_list
            
    def __str__(self):
        return self.in_order()
