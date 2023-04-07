def pisano_period(m):
    current = 1
    old = 0
    for i in range(m * m):
        old, current = current, (old + current) % m
        if old == 0 and current == 1:
            return i + 1

def fibonacci_huge(n, m):
    period = pisano_period(m)
    n = n % period
    
    if n <= 1:
        return n
    
    current = 1
    old = 0
    
    for i in range(n - 1):
        old, current = current, (old + current) % m
    
    return current % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
