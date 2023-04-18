if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    data = [] # (value, 1 - start, 3 - end, 2 - point)
    for _ in range(n):
        val1, val2 = [int(i) for i in input().split()]
        data.append((val1, 1))
        data.append((val2, 3))

    points = [int(x) for x in input().split()]
    assert len(points) == m

    for i in points:
        data.append((i, 2))

    data.sort()

    result = dict()
    counter = 0
    for el in data:
        if el[1] == 1:
            counter += 1
        elif el[1] == 3:
            counter -= 1
        else:
            result[el[0]] = counter

    result_string = ''
    for i in points:
        result_string += str(result[i]) + ' '
    result_string.rstrip()

    print(result_string)
