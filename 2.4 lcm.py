def gcd(a, b):
    if a <= 1 or b <= 1:
        return 1
    current_gcd = a
    old_gcd = b
    if b > a:
        (current_gcd, old_gcd) = (old_gcd, current_gcd)

    while current_gcd != 0:
        (current_gcd, old_gcd) = (old_gcd, current_gcd % old_gcd)
        if old_gcd == 0:
            return current_gcd

    return old_gcd

def lcm(a, b):
    return int((a * b) / gcd(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
