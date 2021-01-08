'''Practice in the writing of algorithms'''


######################################
# Practice day 1 - 05.01.2021
# Practice aim - repeat all algorithms and structures
# which I have read on this moment
######################################


from collections import deque
from time import time

from decorators import print_execution_time_of_function


@print_execution_time_of_function
def get_element_index(element, list_):
    '''Get element index from list'''

    for index, _ in enumerate(list_):
        if list_[index] == element:
            return index

    return 'The element is not in the list'


@print_execution_time_of_function
def get_element_index_by_binary_search(element, list_):
    '''Get element index from list by binary search'''

    lower_index = 0
    highest_index = len(list_) - 1

    while lower_index <= highest_index:
        middle_index = (lower_index + highest_index) // 2
        middle_element = list_[middle_index]

        if element == middle_element:
            return middle_index
        elif element > middle_element:
            lower_index = middle_index + 1
        else:
            highest_index = middle_index - 1

    return 'The element is not in the list'


def is_element_in_graph(element, graph):
    '''Is element in the graph'''

    checked_elements = []

    elements = deque()
    elements += graph[1]

    while elements:
        current_element = elements.popleft()

        # If current_element have been checked already
        if current_element in checked_elements:
            continue

        checked_elements.append(current_element)

        # The element was found
        if current_element == element:
            return True

        # If element was not found
        elements += graph[current_element]

    return False


@print_execution_time_of_function
def sort_list_by_selection(list_):
    '''Sort list by selection'''

    sorted_list = []

    while list_:
        min_element = min(list_)

        sorted_list.append(min_element)
        list_.remove(min_element)

    return sorted_list


def sort_list_by_quick_sort(list_):
    '''Sort list by quick sort'''

    if len(list_) < 2:
        return list_

    # Base element is middle element
    base_element = list_[len(list_) // 2]

    elements_less_than_base_element = [
        element for element in list_ if element < base_element
    ]

    elements_more_than_base_element = [
        element for element in list_ if element > base_element
    ]

    return sort_list_by_quick_sort(elements_less_than_base_element) + \
        [base_element] + \
        sort_list_by_quick_sort(elements_more_than_base_element)


class Stack(object):
    '''Stack class'''

    def __init__(self):
        self.__stack = []

    def add(self, element):
        '''Add element to end of stack'''

        self.__stack.append(element)

    def get(self):
        '''Get element from end of stack'''

        return self.__stack.pop()


class Cell(object):
    '''Cell class for linked list'''

    def __init__(self, value):
        self.value = value
        self.next_cell = None


class LinkedList(object):
    '''Linked list class'''

    def __init__(self):
        self.first_cell = None

    def add(self, value):
        '''Add element to end of linked list'''

        new_cell = Cell(value)

        if self.first_cell is None:
            self.first_cell = new_cell

            return

        # Go to last cell
        last_cell = self.first_cell

        while last_cell.next_cell:
            last_cell = last_cell.next_cell

        last_cell.next_cell = new_cell

    def get(self, cell_index):
        '''Get element from list by index'''

        index_for_iteration = 0
        first_cell = self.first_cell

        while cell_index != index_for_iteration:
            # Go to next cell
            first_cell = first_cell.next_cell

            index_for_iteration += 1

        return first_cell.value


def main():
    '''Run functions for all algorithms and create classes objects'''

    # Search algorithms

    number = 50_000_000
    print(get_element_index(number, list(range(number + 1))))
    print(get_element_index_by_binary_search(number, list(range(number + 1))))

    graph = {
        # 1 level
        1: [2, 3, 4, 5],

        # 2 level
        2: [9, 3],
        3: [],
        4: [8],
        5: [6, 7],

        # 3 level
        9: [],
        8: [],
        6: [],
        7: []
    }

    print(is_element_in_graph(8, graph))

    # Sort

    number = 1_000
    lst = list(range(number))[::-1]
    sort_list_by_selection(lst)

    start_time = time()
    sort_list_by_quick_sort(lst)
    print(time() - start_time)

    # Classes

    stack = Stack()
    stack.add(1)
    stack.add(2)
    stack.add(3)

    print(stack.get())
    print(stack.get())
    print(stack.get())

    linked_list = LinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    print(linked_list.get(0))
    print(linked_list.get(1))
    print(linked_list.get(2))


if __name__ == '__main__':
    main()
