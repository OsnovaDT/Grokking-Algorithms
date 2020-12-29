from functools import wraps
from time import time


def print_execution_time_of_function(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        call_function_time = time()

        function(*args, **kwargs)

        execution_time = round(time() - call_function_time, 4)
        print(
            f'The program was completed in {execution_time} seconds'
        )

    return wrapper
