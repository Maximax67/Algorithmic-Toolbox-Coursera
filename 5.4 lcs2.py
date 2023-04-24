def lcs2(first_sequence, second_sequence):
    matrix = [[0] * (len(second_sequence) + 1) for _ in range(len(first_sequence) + 1)]
    
    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            if (first_sequence[i - 1] == second_sequence[j - 1]):
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    
    return matrix[len(first_sequence)][len(second_sequence)]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert len(a) == n

    m = int(input())
    b = [int(x) for x in input().split()]
    assert len(b) == m

    print(lcs2(a, b))
