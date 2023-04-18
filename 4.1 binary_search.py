def binary_search(keys, query):
    i_min = 0
    i_max = len(keys) - 1
    while i_max >= i_min:
        i_mid = (i_min + i_max) // 2
        if keys[i_mid] == query:
            return i_mid
        if keys[i_mid] < query:
            i_min = i_mid + 1
        else:
            i_max = i_mid - 1
    return -1


if __name__ == '__main__':
    length = int(input())
    input_keys = [int(i) for i in input().split()]
    assert len(input_keys) == length

    length2 = int(input())
    input_queries = [int(i) for i in input().split()]
    assert len(input_queries) == length2

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
