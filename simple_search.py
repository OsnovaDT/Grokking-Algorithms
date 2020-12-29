from decorators import print_execution_time_of_function


@print_execution_time_of_function
def get_element_index(element, list_for_search):
    for index in range(len(list_for_search)):
        if list_for_search[index] == element:
            return f'\nIndex for element {element} is {index}'


if __name__ == '__main__':
    number = 100_000_00
    list_for_search = list(range(1, number + 1))

    print(get_element_index(number, list_for_search))
