def compute_operations(n):
    minNumOperations = [float('inf')] * (n + 1)
    minNumOperations[0] = 0
    minNumOperations[1] = 0
    
    for num in range(2, n + 1):
        results = [float('inf')] * 3
        results[0] = minNumOperations[num - 1] + 1
        if num % 2 == 0:
            results[1] = minNumOperations[num // 2] + 1
        if num % 3 == 0:
            results[2] = minNumOperations[num // 3] + 1
        minNumOperations[num] = min(results)

    sequence = [n]
    while n > 1:
        if n % 2 == 0 and minNumOperations[n] == minNumOperations[n // 2] + 1:
            n //= 2
        elif n % 3 == 0 and minNumOperations[n] == minNumOperations[n // 3] + 1:
            n //= 3
        else:
            n -= 1
        sequence.append(n)
    sequence.reverse()

    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
