def maximum_gold(capacity, weights):
    matrix = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    
    for i in range(1, len(weights) + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                matrix[i][w] = max(matrix[i - 1][w - weights[i - 1]] + weights[i - 1], matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]
    
    return matrix[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n = [int(x) for x in input().split()]
    assert input_capacity >= 0
    input_weights = [int(x) for x in input().split()]
    assert len(input_weights) == n
    
    print(maximum_gold(input_capacity, input_weights))
