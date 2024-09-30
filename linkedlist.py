"""
Exercise: Command Line Linked List Operations

This program manages a singly linked list using command-line arguments.
The linked list supports the following operations:
1. Adding values to the head of the list.
2. Adding values to the tail of the list.
3. Removing the head node of the list.

The program takes command-line input to specify which operation to perform and the value to be added (if applicable).
The program will display the current state of the list after each operation.

Command Line Usage:
1. Add a value to the head of the list:
    python file.py --head <value>
2. Add a value to the tail of the list:
    python file.py --tail <value>
3. Remove the head node from the list:
    python file.py --rmvhead

If an unknown option is provided, the program will return an appropriate error message.

Example:
    python file.py --head "data1"
    python file.py --tail "data2"
    python file.py --rmvhead

The list will be displayed after each operation.

Author : Larose IKITAMA
"""

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_head(self):
        if self.head is not None:
            self.head = self.head.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    if len(sys.argv) < 2:
        print("""
        Command Line Usage:
        1. Add a value to the head of the list:
            python file.py --head <value>
        2. Add a value to the tail of the list:
            python file.py --tail <value>
        3. Remove the head node from the list:
            python file.py --rmvhead
""")
        sys.exit(1)

    llist = LinkedList()
    option = sys.argv[1]

    if option == "--head":
        value = sys.argv[2]
        llist.add_to_head("50")
        llist.add_to_head(" hey i was there before you grrrr!")
        llist.add_to_head(value)
        print("Display")
        llist.display()
    elif option == "--tail":
        value = sys.argv[2]
        llist.add_to_head("one")
        llist.add_to_head("two")
        llist.add_to_head("three")

        llist.add_to_tail(value)
        print("display")
        llist.display()
    elif option == "--rmvhead":
        print("list before")
        llist.add_to_head("one")
        llist.add_to_head("two")
        llist.add_to_head("three")
        llist.display()
        llist.remove_head()
        print("list after")
        llist.display()
    else:
        print(f"unknown option {option}")


if __name__ == "__main__":
    main()
