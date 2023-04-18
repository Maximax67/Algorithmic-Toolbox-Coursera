def binary_search(keys, i_min, i_max, query):
    if i_min >= len(keys):
        return - 1
    if keys[i_min] == query:
        return i_min
    if i_min >= i_max:
        return -1
    mid = i_min + (i_max - i_min) // 2
    if keys[mid] >= query:
        return binary_search(keys, i_min, mid, query)
    return binary_search(keys, mid + 1, i_max, query)


def majority_element(numbers):
    numbers.sort()
    majority = len(numbers) // 2
    number = numbers[majority]

    if number == numbers[0]:
        return 1

    pos = binary_search(numbers, 0, majority, number)
    if pos + majority < len(numbers) and numbers[pos + majority] == number:
        return 1

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = [int(i) for i in input().split()]
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
