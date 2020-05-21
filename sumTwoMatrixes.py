from showMatrix import showMatrix

def sumTwoMatrixes(matrix_a, matrix_b, s, number):
    resultMatrix = []
    for i in range(s):
        row = [0 for i in range(s)];
        resultMatrix.append(row)

    for i in range(s):
        for j in range(s):
            resultMatrix[i][j] = matrix_a[i][j] + matrix_b[i][j]

    print(f"\nSum {number}:")
    showMatrix(s, resultMatrix)
    return resultMatrix

