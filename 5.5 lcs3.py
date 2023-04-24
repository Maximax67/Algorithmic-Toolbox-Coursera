def lcs3(first_sequence, second_sequence, third_sequence):
    matrix = [[[0] * (len(third_sequence) + 1) for _ in range(len(second_sequence) + 1)] for _ in range(len(first_sequence) + 1)]
    
    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            for k in range(1, len(third_sequence) + 1):
                if (first_sequence[i - 1] == second_sequence[j - 1] == third_sequence[k - 1]):
                    matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])
    
    return matrix[len(first_sequence)][len(second_sequence)][len(third_sequence)]

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert len(a) == n

    m = int(input())
    b = [int(x) for x in input().split()]
    assert len(b) == m

    q = int(input())
    c = [int(x) for x in input().split()]
    assert len(c) == q

    print(lcs3(a, b, c))
