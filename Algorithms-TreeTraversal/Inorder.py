class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# A function to do inorder tree traversal
def print_inorder(head):
    if head:
        # First recur on left child
        print_inorder(head.left)

        # then print the data of node
        print(head.data),

        # now recur on right child
        print_inorder(head.right)

    # Driver code
    # if __name__ == "__main__":


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Function call
print("\nInorder traversal of binary tree is")
print_inorder(root)
