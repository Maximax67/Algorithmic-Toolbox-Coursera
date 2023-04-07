def max_pairwise_product(numbers):
    max1 = 0
    max2 = 0
    
    if (numbers[0] > numbers[1]):
        max1 = numbers[0]
        max2 = numbers[1]
    else:
        max1 = numbers[1]
        max2 = numbers[0]
    
    for i in range(2, len(numbers)):
        if (numbers[i] > max2):
            if (numbers[i] > max1):
                max2 = max1
                max1 = numbers[i]
            else:
                max2 = numbers[i]

    return max1 * max2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
