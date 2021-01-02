def get_sum_by_cycle(list_):
    sum_ = 0

    for element in list_:
        sum_ += element

    return sum_


def get_sum_by_recursion(list_, sum_=0):
    if len(list_) == 1:
        return sum_ + list_[0]

    sum_ += list_[0]

    return get_sum_by_recursion(list_[1:], sum_)


def get_amount_elements(list_, amount=0):
    if list_ == []:
        return amount

    return get_amount_elements(list_[1:], amount + 1)


def get_max_number(list_, max_number=0):
    if list_ == []:
        return max_number

    if max_number < list_[0]:
        max_number = list_[0]

    return get_max_number(list_[1:], max_number)


def main():
    list_ = [1, 2, 3, 4, 5, 6, 10]

    print(get_sum_by_cycle(list_))
    print(get_sum_by_recursion(list_))
    print(get_amount_elements(list_))
    print(get_max_number(list_))


if __name__ == '__main__':
    main()
