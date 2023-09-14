import random
import unittest

class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def values(self):
        return [x.value for x in self]

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    @classmethod
    def generate(cls, k, min_value, max_value):
        return cls(random.choices(range(min_value, max_value), k=k))


class DoublyLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, None, self.tail)
            self.tail = self.tail.next
        return self
    
def test_linked_list():
    linked_list = LinkedList()
    
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    
    print("Linked List:")
    for node in linked_list:
        print(node.value)
    
    linked_list.add_to_beginning(0)
    
    print("Updated Linked List:")
    for node in linked_list:
        print(node.value)

test_linked_list()

def test_doubly_linked_list():
    doubly_linked_list = DoublyLinkedList()
    
    doubly_linked_list.add(1)
    doubly_linked_list.add(2)
    doubly_linked_list.add(3)
    
    print("Doubly Linked List (forward):")
    current = doubly_linked_list.head
    while current:
        print(current.value)
        current = current.next
    
    print("Doubly Linked List (backward):")
    current = doubly_linked_list.tail
    while current:
        print(current.value)
        current = current.prev

test_doubly_linked_list()
