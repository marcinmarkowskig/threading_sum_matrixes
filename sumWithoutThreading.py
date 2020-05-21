from sumTwoMatrixes import sumTwoMatrixes
from showMatrix import showMatrix

def sumWithoutThreading(matrix_a, matrix_b, matrix_c, matrix_d, s):
    resultMatrix_1 = sumTwoMatrixes(matrix_a, matrix_b, s, "1")
    resultMatrix_2 = sumTwoMatrixes(matrix_c, matrix_d, s, "2")

