# Singly-linkedList-py
# Python Singly Linked List Implementation

This repository contains a Python implementation of a singly linked list data structure. A singly linked list is a fundamental data structure used to organize and manage data sequentially. It offers various operations for adding, removing, and manipulating data within the list.

## Key Features

- **Insertion**: You can add elements at the beginning, end, or at a specific index in the linked list.
- **Deletion**: Elements can be removed based on their value or index.
- **Printing**: The linked list can be printed to visualize its contents.

## How to Use

1. Initialize a linked list using the `LinkedList` class.
2. Use the provided methods to perform operations on the linked list.

## Function Descriptions

- `insert_at_beginning(data)`: Inserts an element at the beginning of the linked list.

- `insert_at_end(data)`: Inserts an element at the end of the linked list.

- `insert_at(index, data)`: Inserts an element at the specified index in the linked list.

- `insert_values(data_list)`: Takes a list of values as input and creates a new linked list with these values.

- `get_length()`: Returns the length (number of elements) of the linked list.

- `remove_at(index)`: Removes an element at a given index.

- `insert_after_value(data_after, data_to_insert)`: Inserts a new element with `data_to_insert` after the first occurrence of `data_after` in the linked list.

- `remove_by_value(data)`: Removes the first occurrence of an element with the specified `data` value.

## Sample Usage

```python
ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print()
ll.remove_by_value("orange")  # remove orange from the linked list
ll.print()

