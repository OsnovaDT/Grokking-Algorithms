from decorators import print_execution_time_of_function


def get_factorial_by_recursion(number):
    if number == 1:
        return 1
    return number * get_factorial_by_recursion(number - 1)


# For correct decorator's work
@print_execution_time_of_function
def call_function_get_factorial_by_recursion(number):
    get_factorial_by_recursion(number)


@print_execution_time_of_function
def get_factorial_by_cycle(number):
    factorial = 1

    while number != 1:
        factorial *= number
        number -= 1

    return factorial


def main():
    number_for_factorial_calculation = 990

    print('By recursion:')
    call_function_get_factorial_by_recursion(
        number_for_factorial_calculation
    )
    print()

    print('By cycle:')
    get_factorial_by_cycle(number_for_factorial_calculation)


if __name__ == '__main__':
    main()
