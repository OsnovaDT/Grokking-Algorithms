'''Code for tasks from chapter 9'''

from collections import namedtuple


ThingForGrab = namedtuple(
    'Thing_for_grab',
    ['weight', 'price']
)


def print_prices_matrix(prices, subjects_names):
    '''Prints prices in a beautiful way with their string's names'''

    max_len_for_name_in_string_names = len(max(
        subjects_names,
        key=len
    ))

    # Matrix elements
    for string_index, string in enumerate(prices):
        indent = max_len_for_name_in_string_names - \
            len(subjects_names[string_index])
        print(subjects_names[string_index], ' ' * indent, string)


def get_max_price_for_grab(things, max_backpack_size):
    '''Get max possible price fot all the things we can grab'''

    # Set prices to zero
    prices = [
        [0 for _ in range(max_backpack_size)] for _ in things
    ]

    names_of_things_for_grab = list(things.keys())

    # For each string in prices matrix
    for str_index, string in enumerate(prices):
        current_thing = things[
            names_of_things_for_grab[str_index]
        ]
        current_thing_weight = current_thing[0]
        current_thing_price = current_thing[1]

        # For each element in the string
        for element_index in range(len(string)):
            # If the thing doesn't fit in the backpack
            if (element_index + 1) < current_thing_weight:
                # The price = zero
                prices[str_index][element_index] = 0

            # If the thing fits in the backpack
            else:
                # If the string is first
                if str_index == 0:
                    # The price = price for current thing
                    prices[str_index][element_index] = current_thing_price

                # If the string is NOT first
                else:
                    current_price_for_this_weight = \
                        prices[str_index - 1][element_index]

                    remaining_weight = element_index - current_thing_weight
                    if remaining_weight < 0:
                        remaining_weight = 0

                    price_for_remaining_weight = \
                        prices[str_index - 1][remaining_weight]

                    another_price = current_thing_price + price_for_remaining_weight

                    if current_price_for_this_weight > another_price:
                        prices[str_index][element_index] = current_price_for_this_weight
                    else:
                        prices[str_index][element_index] = another_price

    # return prices
    return prices[len(things) - 1][max_backpack_size - 1]


def get_most_similar_word(user_word, similar_words):
    '''Get most similar word on the user's word'''

    coincidence_for_similar_words = {}

    for similar_word in similar_words:
        letters_for_words = list(zip(similar_word, user_word))

        number_of_coincidence = 0

        for similar_word_letter, user_word_letter in letters_for_words:
            if similar_word_letter == user_word_letter:
                number_of_coincidence += 1

        coincidence_for_similar_words[similar_word] = number_of_coincidence

    return max(
        list(coincidence_for_similar_words.items()),
        key=lambda word_and_coincidence: word_and_coincidence[1]
    )[0]


def main():
    '''Apply function get_max_price_for_grab'''

    # Task 1

    things_for_grab = {
        'Recorder': ThingForGrab(4, 3_000),
        'Laptop': ThingForGrab(3, 2_000),
        'Guitar': ThingForGrab(1, 1_500),
        # 'Iphone': ThingForGrab(1, 2_000),
        # 'MP-3': ThingForGrab(1, 1_000),
    }

    max_backpack_size = 4

    # print_prices_matrix(
    # get_max_price_for_grab(things_for_grab, max_backpack_size),
    # [name for name in things_for_grab]
    # )

    print(get_max_price_for_grab(things_for_grab, max_backpack_size))

    # Task 2

    user_word = 'hish'
    similar_words = ['fish', 'vista']

    print(get_most_similar_word(user_word, similar_words))


if __name__ == '__main__':
    main()
