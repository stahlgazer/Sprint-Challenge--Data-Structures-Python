class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        print(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next_node

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # no list exists
        if self.head is None:
            return None
        # if node reaches the end / is only node
        if node.get_next() == None:
            # node becomes head
            self.head = node
            return

        # else start recursively reversing
        next_node = node.get_next()
        self.reverse_list(next_node, node)

        node.get_next().set_next(node)
        node.set_next(None)

LL = LinkedList()
gav = LL.add_to_head('I')
test = LL.add_to_head('AM')
newhead = LL.add_to_head('REVERSED')
LL.printList()
LL.reverse_list(LL.head, LL.head.next_node)
print("List Now Reversed: ")
LL.printList()

