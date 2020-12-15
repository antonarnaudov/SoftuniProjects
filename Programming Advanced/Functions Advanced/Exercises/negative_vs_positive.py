def nvp(numbers):
    positive = []
    negative = []

    for n in numbers:
        if n > 0:
            positive.append(n)
            continue
        negative.append(n)
    print(sum(negative))
    print(sum(positive))
    if abs(sum(negative)) > sum(positive):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nvp([int(x) for x in input().split()])


# ----------------------------------------------------------------- #


def nvp_two(nums):
    negative_sum = sum(filter(lambda x: x < 0, nums))
    positive_sum = sum(filter(lambda x: x > 0, nums))

    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nvp_two([int(x) for x in input().split()])
