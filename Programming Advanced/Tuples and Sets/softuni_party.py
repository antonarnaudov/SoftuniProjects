def get_not_arrived_guests(guests, guests_arrived):
    # guests_set = set(guests)
    # [guests_set.remove(guests) for guests in guests if guests_arrived]
    # return giests_set
    return set(guests) - set(guests_arrived)


def print_result(result):
    result = sorted(result)
    print(len(result))
    [print(guest) for guest in result if guest[0].isdigit()]
    [print(guest) for guest in result if not guest[0].isdigit()]


print_result(input())
