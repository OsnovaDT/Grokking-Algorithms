'''Contains some useful decorators'''


from functools import wraps
from time import time


def print_execution_time_of_function(function):
    '''Print print execution time of function'''

    @wraps(function)
    def wrapper(*args, **kwargs):
        call_function_time = time()

        result = function(*args, **kwargs)

        execution_time = round(time() - call_function_time, 7)
        print(
            f'The program was completed in {execution_time} seconds'
        )

        return result

    return wrapper
