def optimal_summands(n):
    if n == 0:
        return [0]

    counter = 1
    current_sum = 0
    summands = []

    while current_sum < n:
        if (current_sum + counter * 2 + 1 <= n):
            summands.append(counter)
            current_sum += counter
            counter += 1
        else:
            summands.append(n - current_sum)
            break

    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
