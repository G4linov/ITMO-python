"""
Лаболаторная №1
Этап 1:
Создать исходную матрицу для траснпортирования NxM
При помощи рандомайзера

Этап 2:
Транспонировать матрицу NxM

Контрольный пример:
1 2 3   ->  1 3
3 4 5       2 4
            3 5

Этап 3*:

"""

import random

n = int(input("Введите число строк: "))
m = int(input("Введите число столбцов: "))

matrixIn = []
matrixOut = []

for i in range(n):
    matrixIn.append([])
    for j in range(m):
        matrixIn[i].append(random.randint(0,100))

print("Исходная матрица:")
for i in range(n):
    print(*matrixIn[i], sep=' ')

for i in range(m):
    matrixOut.append([])
    for j in range(n):
        matrixOut[i].append(matrixIn[j][i])

print("\nТранспонированная матрица:")
for i in range(m):
    print(*matrixOut[i], sep=' ')
