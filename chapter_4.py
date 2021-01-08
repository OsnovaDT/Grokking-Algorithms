'''Code for chapter 4'''

from time import time

from selection_sort import sort_list_by_selection


def get_sum_by_cycle(list_):
    '''Get sum of elements by cycle'''

    sum_ = 0

    for element in list_:
        sum_ += element

    return sum_


def get_sum_by_recursion(list_, sum_=0):
    '''Get sum of elements by recursion'''

    if len(list_) == 1:
        return sum_ + list_[0]

    sum_ += list_[0]

    return get_sum_by_recursion(list_[1:], sum_)


def get_amount_elements(list_, amount=0):
    '''Get amount of elements in list'''

    if list_ == []:
        return amount

    return get_amount_elements(list_[1:], amount + 1)


def get_max_number(list_, max_number=0):
    '''Get max number from list'''

    if list_ == []:
        return max_number

    if max_number < list_[0]:
        max_number = list_[0]

    return get_max_number(list_[1:], max_number)


def quick_sort(list_):
    '''Sort list by quick sort'''

    if len(list_) < 2:
        return list_

    # With this condition the program will work faster
    if (len(list_) == 2) and (list_[0] > list_[1]):
        list_[0], list_[1] = list_[1], list_[0]

        return list_

    middle_list_element = list_[len(list_) // 2]

    elements_less_than_middle_element = [
        element for element in list_ if element < middle_list_element
    ]

    elements_more_than_middle_element = [
        element for element in list_ if element > middle_list_element
    ]

    return quick_sort(elements_less_than_middle_element) + \
        [middle_list_element] + \
        quick_sort(elements_more_than_middle_element)


def main():
    '''Run all functions for chapter 4'''

    list_ = list(range(100))

    print(get_sum_by_cycle(list_))
    print(get_sum_by_recursion(list_))
    print(get_amount_elements(list_))
    print(get_max_number(list_))

    # Quick sort works faster than sort by selection (simple sort)
    print('Sort by selection')
    sort_list_by_selection(list_[::-1])

    print('\nQuick sort')
    start = time()
    quick_sort(list_[::-1])
    print(f'The program was completed in {time() - start} seconds')


if __name__ == '__main__':
    main()
