'''Calculating factorial for chapter 3'''


from time import time

from decorators import print_execution_time_of_function


def get_factorial_by_recursion(number):
    '''Calculate factorial by recursion'''

    if number == 1:
        return 1

    return number * get_factorial_by_recursion(number - 1)


@print_execution_time_of_function
def get_factorial_by_cycle(number):
    '''Calculate factorial by cycle'''

    factorial = 1

    while number != 1:
        factorial *= number
        number -= 1

    return factorial


def main():
    '''Run functions for calculating factorial'''

    number_for_factorial_calculation = 990

    print('By recursion:')
    start = time()
    get_factorial_by_recursion(
        number_for_factorial_calculation
    )
    print(f'The program was completed in {time() - start} seconds')

    print('By cycle:')
    get_factorial_by_cycle(number_for_factorial_calculation)


if __name__ == '__main__':
    main()
