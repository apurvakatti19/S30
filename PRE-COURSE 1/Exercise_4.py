#BINARY TREE

class Node:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
        
def insert(root,node):
    if root is None:
        root = node
    else:
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.value)
        Inorder(root.right)

if __name__ == "__main__":
    root = Node(110)
    insert(root,Node(12))
    insert(root,Node(23))
    insert(root,Node(88))
    insert(root,Node(287))
    insert(root,Node(115))
    insert(root,Node(234))
    Inorder(root)