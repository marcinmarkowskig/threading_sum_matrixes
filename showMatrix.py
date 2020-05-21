def showMatrix(s, matrix):
    for i in range(s):
        for j in range(s):
            print(matrix[i][j], end = "  ")
            if matrix[i][j] < 10:
                print(end=" ")
        print()
