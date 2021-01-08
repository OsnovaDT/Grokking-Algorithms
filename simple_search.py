'''Simple search for chapter 1'''


from decorators import print_execution_time_of_function


@print_execution_time_of_function
def get_element_index(element, list_for_search):
    '''Get element index from the list'''

    for index, _ in enumerate(list_for_search):
        if list_for_search[index] == element:
            return f'\nIndex for element {element} is {index}'

    return "Was not found the element's index"


def main():
    '''Run get_element_index function'''

    number = 10_000_000
    list_for_search = list(range(1, number + 1))

    print(get_element_index(number, list_for_search))


if __name__ == '__main__':
    main()
