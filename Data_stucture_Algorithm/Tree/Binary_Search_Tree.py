class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    # Insert an data in tree
    def insert(self,data):
        newnode=Node(data)
        if self.root is None:
            self.root=newnode
            return
        
        current_node=self.root
        while True:
            if data<current_node.data:
                if current_node.left is None:
                    current_node.left=newnode
                    break
                else:
                    current_node=current_node.left

            elif data>current_node.data:
                if current_node.right is None:
                    current_node.right=newnode
                    break
                else:
                    current_node=current_node.right
    
    # Print Inorder travarsal(Root,Left,Right)
    def inorder_traversal(self,root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.data)
        self.inorder_traversal(root.right)
    
    def preorder_traversal(self,root):
        if root is None:
            return
        print(root.data,end=" -> ")
        self.inorder_traversal(root.left)
        self.inorder_traversal(root.right)


bst=BinarySearchTree()
bst.insert(50)
bst.insert(20)
bst.insert(30)
bst.insert(80)
bst.insert(10)
bst.insert(40)
bst.insert(100)
bst.insert(70)
bst.insert(60)
bst.inorder_traversal(bst.root)
bst.preorder_traversal(bst.root)