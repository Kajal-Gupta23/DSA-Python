class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# A function to do inorder tree traversal
def print_postorder(head):
    if head:
        print_postorder(head.left)
        print_postorder(head.right)
        print(head.data),


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\nPostorder traversal of binary tree is")
    print_postorder(root)
