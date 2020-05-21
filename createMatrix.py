import random

def createMatrix(s, matrix):
    for i in range(s):
        row = [random.randrange(1, 10, 1) for i in range(s)];
        matrix.append(row)
    return matrix

