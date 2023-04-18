def merge(array, temp, left, mid, right):
    inv_count = 0
    i = left
    j = mid
    k = left
    while (i <= mid - 1 and j <= right):
        if (array[i] <= array[j]):
            temp[k] = array[i]
            k += 1
            i += 1
        else:
            temp[k] = array[j]
            k += 1
            j += 1
            inv_count += mid - i

    while (i <= mid - 1):
        temp[k] = array[i]
        k += 1
        i += 1

    while (j <= right):
        temp[k] = array[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        array[i] = temp[i]

    return inv_count


def mergeSort(array, temp, left, right):
    mid = 0
    inv_count = 0
    if (right > left):
        mid = int((right + left) / 2)
        inv_count = mergeSort(array, temp, left, mid)
        inv_count += mergeSort(array, temp, mid + 1, right)
        inv_count += merge(array, temp, left, mid + 1, right)
    return inv_count


def countInversions(array):
    temp = [0] * len(array)
    return mergeSort(array, temp, 0, len(array) - 1)


if __name__ == '__main__':
    input_n = int(input())
    elements = [int(i) for i in input().split()]
    assert len(elements) == input_n
    print(countInversions(elements))
