def fibonacci_sum(n):
    if n <= 1:
        return n
    
    current = 1
    old = 0
    
    for i in range((n + 2) % 60):
        (old, current) = (current, (old + current) % 10)

    if old == 0:
        return 9

    return old - 1

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
