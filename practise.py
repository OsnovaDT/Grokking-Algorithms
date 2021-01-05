
######################################
# Practice day 1 - 05.01.2021
######################################


from collections import deque
from time import time

from decorators import print_execution_time_of_function


@print_execution_time_of_function
def get_element_index(element_for_search, list_):
    for index in range(len(list_)):
        if list_[index] == element_for_search:
            return index

    return 'The element is not in the list'


@print_execution_time_of_function
def binary_search(element_for_search, list_):
    lower_index = 0
    highest_index = len(list_) - 1

    while lower_index <= highest_index:
        middle_index = (lower_index + highest_index) // 2
        middle_element = list_[middle_index]

        if element_for_search == middle_element:
            return middle_index
        elif element_for_search > middle_element:
            lower_index = middle_index + 1
        else:
            highest_index = middle_index - 1

    return 'The element is not in the list'


def find_element_in_graph(element, graph):
    checked_elements = []

    elements = deque()
    elements += graph[1]

    while elements:
        current_element = elements.popleft()

        if current_element in checked_elements:
            continue

        checked_elements.append(current_element)

        print(current_element)
        if current_element == element:
            return 'The element found'

        elements += graph[current_element]


@print_execution_time_of_function
def sort_list_by_selection(list_):
    sorted_list = []

    while list_:
        min_element = min(list_)

        sorted_list.append(min_element)
        list_.remove(min_element)

    return sorted_list


def fast_sort(list_):
    if len(list_) < 2:
        return list_
    base_element = list_[len(list_) // 2]

    elements_less_than_base_element = [
        element for element in list_ if element < base_element
    ]

    elements_more_than_base_element = [
        element for element in list_ if element > base_element
    ]

    return fast_sort(elements_less_than_base_element) + [base_element] + fast_sort(elements_more_than_base_element)


def main():
    # Search

    # number = 50_000_000
    # print(get_element_index(number, list(range(number + 1))))
    # print(binary_search(number, list(range(number + 1))))

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

    # print(find_element_in_graph(8, graph))

    # Sort

    # number = 1_000
    # lst = list(range(number))[::-1]
    # sort_list_by_selection(lst)

    # start = time()
    # fast_sort(lst)
    # print(time() - start)


if __name__ == '__main__':
    main()
