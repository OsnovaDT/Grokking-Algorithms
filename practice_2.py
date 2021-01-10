'''Practice in the writing of algorithms'''


######################################
# Practice day 2 - 10.01.2021
# Practice aim - repeat all algorithms and structures
# which I have read in book 'Grokking Algorithms'
######################################

from time import time
from collections import deque

from decorators import print_execution_time_of_function


@print_execution_time_of_function
def get_item_index_by_simple_search(item, list_):
    '''Simple search for an item in a list'''

    for item_index, list_item in enumerate(list_):
        if list_item == item:
            return item_index

    return None


@print_execution_time_of_function
def get_item_index_by_binary_search(item, list_):
    '''Binary search for an item in a list'''

    lower_index = 0
    upper_index = len(list_) - 1

    while lower_index <= upper_index:
        middle_index = (lower_index + upper_index) // 2
        middle_item = list_[middle_index]

        if item == middle_item:
            return middle_index

        if item < middle_item:
            upper_index = middle_index - 1
        else:
            lower_index = middle_index + 1

    return None


@print_execution_time_of_function
def sort_list_by_simple_sort(list_):
    '''Simple sort for list'''

    list_for_sorting = list_.copy()
    sorted_list = []

    while list_for_sorting:
        min_item = min(list_for_sorting)

        sorted_list.append(min_item)

        list_for_sorting.remove(min_item)

    return sorted_list


def sort_list_by_quick_sort(list_):
    '''Quick sort for list'''

    if len(list_) < 2:
        return list_

    base_item = list_[len(list_) // 2]

    items_smaller_than_base_item = [
        item for item in list_ if item < base_item
    ]

    items_more_than_base_item = [
        item for item in list_ if item > base_item
    ]

    return sort_list_by_quick_sort(items_smaller_than_base_item) + \
        [base_item] + \
        sort_list_by_quick_sort(items_more_than_base_item)


def go_around_the_tree_in_width(tree, starting_node='A'):
    '''Traversing the tree in width'''

    nodes = deque(tree[starting_node])

    while nodes:
        next_node = nodes.popleft()

        print(next_node, end=' --> ')

        # Add neighbours for next_node
        nodes.extend(tree[next_node])

    print()


def go_around_the_tree_in_depth(tree, starting_node='A'):
    '''Traversing the tree in depth'''

    for first_neighbour_for_starting_node in tree[starting_node]:
        print(first_neighbour_for_starting_node, end=' --> ')

        go_around_the_tree_in_depth(
            tree,
            first_neighbour_for_starting_node
        )


class Stack():
    '''Simple stack'''

    def __init__(self):
        self.__stack = []

    def add(self, value):
        '''Add value to the end of stack'''

        self.__stack.append(value)

    def get(self):
        '''Get a value from the end of stack'''

        return self.__stack.pop()


class Cell():
    '''Cell for save value for linked list'''

    def __init__(self, value):
        self.value = value
        self.next_cell = None


class LinkedList():
    '''Linked list'''

    def __init__(self):
        self.first_cell = None

    def add(self, value):
        '''Add new cell with value to linked list'''

        new_cell = Cell(value)

        # If the linked list is empty
        if self.first_cell is None:
            self.first_cell = new_cell

            return

        first_cell = self.first_cell

        while first_cell.next_cell:
            # Go to next cell
            first_cell = first_cell.next_cell

        first_cell.next_cell = new_cell

    def get(self, cell_index):
        '''Get cell by index'''

        index = 0

        first_cell = self.first_cell

        while first_cell.next_cell and (index != cell_index):
            first_cell = first_cell.next_cell
            index += 1

        return first_cell.value


def main():
    '''Run all functions and classe's functions'''

    # Simple and binary search

    number = 10_000_000
    items = list(range(number + 1))

    # Simple search
    print(get_item_index_by_simple_search(number, items))

    # Binary search
    print(get_item_index_by_binary_search(number, items))

    # Simple and quick sort

    list_for_sorting = list(range(10_000))[::-1]

    # Simple sort
    sort_list_by_simple_sort(list_for_sorting)

    # Quick sort
    start_time = time()
    sort_list_by_quick_sort(list_for_sorting)
    print(
        f'The program was completed in {round(time() - start_time, 7)} seconds'
    )

    # Traversing a tree in width and in depth

    tree = {
        # Level 1
        'A': ['B', 'C', 'D'],

        # Level 2
        'B': [],
        'C': ['Z'],
        'D': ['F', 'E'],

        # Level 3
        'Z': [],
        'F': [],
        'E': [],
    }

    # Traversing a tree in width

    go_around_the_tree_in_width(tree)

    # Traversing a tree in depth

    go_around_the_tree_in_depth(tree)

    print()

    # Structures

    # Stack

    stack = Stack()

    stack.add(1)
    stack.add(2)
    stack.add(3)

    print(stack.get())
    print(stack.get())
    print(stack.get())

    # Linked list

    linked_list = LinkedList()

    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    print(linked_list.get(0))
    print(linked_list.get(1))
    print(linked_list.get(2))


if __name__ == '__main__':
    main()
