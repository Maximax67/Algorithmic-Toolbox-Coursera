from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    first_sequence.sort()
    second_sequence.sort()
    product = 0

    for i in range(len(first_sequence)):
        product += first_sequence[i] * second_sequence[i]

    return product


if __name__ == '__main__':
    n = int(input())
    prices = [int(i) for i in input().split()]
    clicks = [int(i) for i in input().split()]
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

