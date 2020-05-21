from createMatrix import createMatrix
from showMatrix import showMatrix
from sumThreading import sumThreading
from sumWithoutThreading import sumWithoutThreading
import time

print('Enter the size of square matrix: ');
s = int(input());

matrix = []

print('\n\nMatrix 1')
matrix1 = createMatrix(s, matrix)
showMatrix(s, matrix1)
matrix = []
print('\n\nMatrix 2')
matrix2 = createMatrix(s, matrix)
showMatrix(s, matrix2)
matrix = []
print('\n\nMatrix 3')
matrix3 = createMatrix(s, matrix)
showMatrix(s, matrix3)
matrix = []
print('\n\nMatrix 4')
matrix4 = createMatrix(s, matrix)
showMatrix(s, matrix4)
matrix = []

print('\n\nRESULTS WITH THREADS')
before_time = time.time()
print('\nTime before: ', before_time)
sumThreading(matrix1, matrix2, matrix3, matrix4, s)
after_time = time.time()
print('\nTime after: ', after_time)
difference_thread = after_time - before_time

print('\n\nRESULTS WITHOUT THREADS')
before_time_2 = time.time()
print('\nTime before: ', before_time_2)
sumWithoutThreading(matrix1, matrix2, matrix3, matrix4, s)
after_time_2 = time.time()
print('\nTime after: ', after_time_2)
difference_without_thread = after_time_2 - before_time_2

print('\n\n')
print('DIFFERENCE WITH THREADS', difference_thread)
print('DIFFERENCE WITHOUT THREADS', difference_without_thread)

plik = open('wyniki1.txt','a')
plik.writelines(["50", " ", str(difference_thread), " ", str(difference_without_thread), "\n"])
plik.close()
time.sleep(10)

