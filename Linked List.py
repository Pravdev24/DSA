class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head == None:
               print("Linked list is empty")
        else:
            n = self.head
            while n != None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = new_node

    def add_after(self, value, data):        
        n = self.head
        while n != None:
            if n.data == value:
                break
            n = n.ref
        if n == None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, value, data):
        if self.head == None:
            print("linked List is empty")
        else:
            if self.head.data == value:
                self.add_begin(data)
            else:
                n = self.head
                while n.ref != None:
                    if n.ref.data == value: # iterting the next value data n.ref.data
                        break
                    n = n.ref
                if n == None:
                    print("Node is not found")
                else:
                    new_node = Node(data)
                    new_node.ref = n.ref
                    n.ref = new_node

    def delete_begin(self):
        if self.head == None:
            print("Linked list is empty you cannot delete nodes")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head == None:
            print("Linked list is empty you cannot delete nodes")
        elif self.head == None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref != None:
                n = n.ref
            n.ref = None

    def delete_between(self, value):
        if self.head == None:
            print("You cannot delete a node linked list is empty")
        elif self.head.data == value:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref != None:
                if n.ref.data == value:
                    break
                else:
                    n = n.ref
            if n.ref == None:
                print("Node not in the Linked List")
            else:
                n.ref = n.ref.ref
            



LL = LinkedList()
list = ["banana", "apple", "orange", "guava"]
for i in list:
    LL.add_end(i)


LL.print_ll()

