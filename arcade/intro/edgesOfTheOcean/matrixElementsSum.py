def solution(matrix):
    l = len(matrix)
    sum = 0
    for i in range(l):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                if(i < l - 1):
                    matrix[i+1][j] = 0
            sum = sum + matrix[i][j]
    return sum