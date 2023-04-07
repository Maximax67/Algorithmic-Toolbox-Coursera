def fibonacci_number(n):
    if n <= 1:
        return n
    current = 1
    old = 1
    for i in range(2, n):
        (current, old) = (current + old, current)

    return current


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
