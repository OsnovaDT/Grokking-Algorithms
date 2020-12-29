from decorators import print_execution_time_of_function


@print_execution_time_of_function
def search_number_in_list(number, list_for_search):
    for element in list_for_search:
        if element == number:
            print('You guessed')
            break


if __name__ == '__main__':
    number = 100_000_000
    list_for_search = list(range(1, number + 1))

    search_number_in_list(number, list_for_search)
