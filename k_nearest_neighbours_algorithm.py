'''Code for task in chapter 10'''


from collections import namedtuple
from math import sqrt


def get_the_most_similar_parameter(
        parameter, other_parameters):
    '''Get the most similar parameter'''

    # The most similar parameter and his difference with parameter's values
    the_most_similar_parameter = None, float('inf')

    for another_parameter, another_parameter_values in other_parameters.items():
        parameter_and_another_parameter_values = zip(
            parameter, another_parameter_values
        )

        difference_between_parameters_values = sqrt(sum([
            (values[0] - values[1]) ** 2 for values in parameter_and_another_parameter_values
        ]))

        # If difference between parameter values less than current smallest difference
        if difference_between_parameters_values < the_most_similar_parameter[1]:
            the_most_similar_parameter = another_parameter, difference_between_parameters_values

    # Name of the most similar parameter
    return the_most_similar_parameter[0]


def get_k_most_similar_parameters(parameter, other_parameters, k=1):
    '''Get k most similar parameters for the parameter'''

    other_parameters_copy = other_parameters.copy()
    k_most_similar_parameters = []

    while k:
        the_most_similar_parameter = get_the_most_similar_parameter(
            parameter, other_parameters_copy
        )

        k_most_similar_parameters.append(the_most_similar_parameter)

        other_parameters_copy.pop(the_most_similar_parameter)

        k -= 1

    return k_most_similar_parameters


def main():
    '''Run function get_the_most_similar_parameter'''

    # Task 1 - Classification
    UserRating = namedtuple(
        'UserRating',
        [
            'Comedy',
            'Action_movie',
            'Drama',
            'Horror',
            'Melodrama'
        ]
    )

    current_user_ratings = UserRating(3, 4, 4, 1, 4)

    other_users_ratings = {
        'Justin': UserRating(4, 3, 5, 1, 5),
        'Morpheus': UserRating(2, 5, 1, 3, 1),
    }

    print(get_the_most_similar_parameter(
        current_user_ratings, other_users_ratings
    ))

    # Task 2 - Regression

    DayCondition = namedtuple(
        'DayCondition',
        [
            'Weather',
            'IsHoliday',
            'ThereIsSportGame',
        ]
    )

    today_condition = DayCondition(4, 1, 0)

    other_days_conditions = {
        'A': DayCondition(5, 1, 0),
        'B': DayCondition(3, 1, 1),
        'C': DayCondition(1, 1, 0),
        'D': DayCondition(4, 0, 1),
        'E': DayCondition(4, 0, 0),
        'F': DayCondition(2, 0, 0),
    }

    print(get_k_most_similar_parameters(
        today_condition, other_days_conditions, 4
    ))

    print(get_k_most_similar_parameters(
        today_condition, other_days_conditions, 4
    ))


if __name__ == '__main__':
    main()
