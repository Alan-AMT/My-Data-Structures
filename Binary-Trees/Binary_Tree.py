from Binary_Tree_Interface import BinaryTreeInterface

class BinaryTree(BinaryTreeInterface):
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None
    
    #Traversal functions are meant to return a list with all the roots of the tree
    def pre_order(main_root):
        pre_order_values = []
        
        def get_pre_order(sub_tree):
            if sub_tree:
                get_pre_order(sub_tree.left)
                pre_order_values.append(sub_tree.root)
                get_pre_order(sub_tree.right)
                
        get_pre_order(main_root)
        return pre_order_values
            
    def in_order(main_root):
        in_order_values = []
        
        def get_in_order(sub_tree):
            if sub_tree:
                get_in_order(sub_tree.left)
                in_order_values.append(sub_tree.root)
                get_in_order(sub_tree.right)
                
        get_in_order(main_root)
        return in_order_values
            
    def post_order(main_root):
        post_order_values = []
        
        def get_post_order(sub_tree):
            if sub_tree:
                get_post_order(sub_tree.left)
                get_post_order(sub_tree.right)
                post_order_values.append(sub_tree.root)

        get_post_order(main_root)
        return post_order_values
            
    def __str__(self):
        print(*self.in_order(), end="")
        return ""
