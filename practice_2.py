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


def main():
    '''Run all functions for test'''

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


if __name__ == '__main__':
    main()
