class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data=None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        current = self.head
        my_string = ""
        while current:
            my_string += f"{current.data} -> "
            current = current.next
        my_string += "None"
        return my_string

    def retrieve_x_node(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("index out of range")
            current = current.next
        if current is None:
            raise IndexError("index out of range")
        return current

    def has_cycle(self):
        p1 = self.head
        p2 = self.head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

linked_list = LinkedList(10)
linked_list.append(1)
linked_list.append("this is a string")
linked_list.append(3)
print(linked_list)
print(linked_list.has_cycle())

# Creating a cycle for testing purposes (Not part of the LinkedList class)
last_node = linked_list.retrieve_x_node(2)
first_node = linked_list.head
last_node.next = first_node
print(linked_list.has_cycle())