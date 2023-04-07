def IsBetter(number1, number2):
    return int(str(number1) + str(number2)) >= int(str(number2) + str(number1))

def largest_number(numbers):
    largest = []
    
    while numbers != []:
        best_number = 0
        for number in numbers:
            if IsBetter(number, best_number):
                best_number = number
        largest.append(best_number)
        numbers.remove(best_number)
    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = [int(i) for i in input().split()]
    print(*largest_number(input_numbers), sep='')
