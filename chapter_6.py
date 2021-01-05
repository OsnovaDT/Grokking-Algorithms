from collections import deque


# For ordered friends_network
def find_mango_seller_v1(friends_network, mango_seller):
    for friend in friends_network:
        friends_for_current_friend = friends_network[friend]

        if mango_seller in friends_for_current_friend:
            return 'Found'


# For ordered or NOT ordered friends_network
def find_mango_seller_v2(friends_network):
    checked_friends = []

    # We also can use Queue here, but code will be more long
    friends = deque()
    friends += friends_network['Me']

    while friends:
        current_friend = friends.popleft()

        if current_friend in checked_friends:
            # Go to next current_friend
            continue

        # If current_friend not in checked_friends
        checked_friends.append(current_friend)

        # We found the mango seller
        if is_mango_seller(current_friend):
            return 'Found'

        # Add all friends for current friend to friends queue
        friends += friends_network[current_friend]

    if not friends:
        return 'The mango seller was not found'


def is_mango_seller(person):
    return person == 'Tom'


def main():
    friends_network = {
        # The first level
        'Me': ['Bob', 'Alice', 'Claire'],

        # The second level
        'Bob': ['Anuj', 'Peggy'],
        'Alice': ['Peggy'],
        'Claire': ['Tom', 'Jonny'],

        # # The third level
        'Anuj': [],
        'Peggy': [],
        'Tom': [],
        'Jonny': [],
    }

    print(find_mango_seller_v2(friends_network))


if __name__ == '__main__':
    main()
