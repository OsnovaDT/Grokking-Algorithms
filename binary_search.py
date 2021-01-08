'''Binary search for chapter 1'''

from decorators import print_execution_time_of_function


# Binary search
@print_execution_time_of_function
def get_element_index(element, list_for_search):
    '''Get element index by binary search'''

    lower_index = 0
    upper_index = len(list_for_search) - 1

    while lower_index <= upper_index:
        middle_index = (lower_index + upper_index) // 2
        middle_element = list_for_search[middle_index]

        if element == middle_element:
            return f'\nIndex for element {element} is {middle_index}'
        elif element < middle_element:
            upper_index = middle_index - 1
        else:
            lower_index = middle_index + 1


def main():
    '''Run function get_element_index'''
    number = 50_000_000
    list_for_search = list(range(1, number + 1))
    print(get_element_index(number, list_for_search))


if __name__ == '__main__':
    main()
