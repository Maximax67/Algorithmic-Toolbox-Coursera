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


if __name__ == '__main__':
    length = int(input())
    input_keys = [int(i) for i in input().split()]
    assert len(input_keys) == length

    length2 = int(input())
    input_queries = [int(i) for i in input().split()]
    assert len(input_queries) == length2

    for q in input_queries:
        print(binary_search(input_keys, 0, length, q), end=' ')

