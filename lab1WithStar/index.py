#import numpy as np
import random
print("Лабораторная работа №1* \n")
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = []
for i in range(m):
    matrix.append([])
    for g in range(n):
        matrix[i].append(random.randint(0, 100))
for el in matrix:
    print(el)

matrix2 = []
for i in range(n):
    matrix2.append([])
    for g in range(m):
        matrix2[i].append(matrix[g][i])

for el in matrix2:
    print(el)
if n == m:
    matrix = np.array(matrix)
    d = np.linalg.det(matrix)
    print("Определитель матрицы равен ", d)   
else:
    print("матрица не квадратная")