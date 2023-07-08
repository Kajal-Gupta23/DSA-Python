class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def print_preorder(head):
    if head:
        print(head.data),

        print_preorder(head.left)

        print_preorder(head.right)


# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)

    # Function call
    print("\nPreorder traversal of binary tree is")
    print_preorder(root)
