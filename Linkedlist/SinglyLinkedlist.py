class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# create class to link nodes
class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    # add element in the beginning, in the end, in between
    # 1)create node, 2)next node ref = head

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            n = self.head
            while n.ref is not None:
                n = n.ref

            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)

            new_node.ref = self.head
            self.head = new_node
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("ll is not empty")

    def delete_begin(self):
        if self.head is None:
            print("no nodes to delete")

        else:
            self.head = self.head.ref

    # check if list is empty
    # get the 2nd last element and set its reference to none
    def delete_end(self):
        if self.head is None:
            print("no nodes to delete")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref

            n.ref = None

    # delete given node
    # first check if ll is empty then check if its first node if true then head= 2nd node
    # if its not 1st node then go to its previous node change its ref

    def delete_by_value(self,x):
        if self.head is None:
            print("no nodes to delete")
            return

        if self.head.data == x:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n = n.ref
        if n.ref is None:
            print("element not found")
        else:
            n.ref = n.ref.ref






# n1 = Node(10)
ll = LinkedList()
# ll.insert_empty(10)
# ll.insert_empty(20)
ll.add_begin(30)
ll.add_begin(00)

ll.add_end(20)
ll.add_end(50)
ll.add_before(40, 20)
ll.add_before(30, 50)
# ll.delete_end()
# ll.delete_begin()
ll.delete_by_value(30)
ll.print_ll()
