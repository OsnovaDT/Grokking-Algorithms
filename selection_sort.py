from random import randint

my_list = [randint(1, 100) for _ in range(10)]


def get_minimum_value_from_list(initial_list):
    minimum_value = initial_list[0]

    for value in initial_list:
        if value < minimum_value:
            minimum_value = value

    return minimum_value


def sort_list_by_selection(initial_list):
    final_list = []

    for _ in range(len(initial_list)):
        minimum_value_from_initial_list = get_minimum_value_from_list(
            initial_list
        )
        final_list.append(minimum_value_from_initial_list)
        initial_list.remove(minimum_value_from_initial_list)

    return final_list


print(my_list)
print(sort_list_by_selection(my_list))
