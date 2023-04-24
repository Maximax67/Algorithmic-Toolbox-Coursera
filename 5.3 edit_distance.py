def edit_distance(first_string, second_string):
    matrix = [[float('inf')] * (len(second_string) + 1) for _ in range(len(first_string) + 1)]
    
    for i in range(len(first_string) + 1):
        matrix[i][0] = i
    
    for i in range(1, len(second_string) + 1):
        matrix[0][i] = i
    
    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            matrix[i][j] = min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1] + int(first_string[i - 1]!=second_string[j - 1]))
    
    return matrix[len(first_string)][len(second_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
