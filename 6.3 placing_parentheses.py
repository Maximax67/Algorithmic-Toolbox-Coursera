def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(d, op):
    def MinAndMax(i, j):
        min_val = float('inf')
        max_val = float('-inf')
        for k in range(i, j):
            a = evaluate(M[i][k], M[k + 1][j], op[k])
            b = evaluate(M[i][k], m[k + 1][j], op[k])
            c = evaluate(m[i][k], M[k + 1][j], op[k])
            d = evaluate(m[i][k], m[k + 1][j], op[k])
            min_val = min(min_val, a, b, c, d)
            max_val = max(max_val, a, b, c, d)
        return min_val, max_val
    
    n = len(d)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    
    for i in range(n):
        m[i][i] = d[i]
        M[i][i] = d[i]
    
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j)
    
    return M[0][n - 1]


def split_input(input_string):
    numbers = []
    operations = []
    digit = 0
    for i in input_string:
        if i.isdigit():
            digit = digit * 10 + int(i)
        else:
            numbers.append(digit)
            operations.append(i)
            digit = 0
    numbers.append(digit)
    return numbers, operations


if __name__ == "__main__":
    print(maximum_value(*split_input(input())))
