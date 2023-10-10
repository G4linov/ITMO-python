"""
Бинарный поиск
"""

n = int(input("Введите число: "))

befind = []
finded = False

for i in range(1000,1500):
    befind.append(i)

right = len(befind)
left = 0

if n > befind[right - 1] or n < befind[0]:
    print("Числа нет в списке")
else:
    while not finded:

        if (n == befind[mid]):
            print("Число n лежит под индексом", right)
            finded = True
        elif (n > befind[mid]):
            left = right / 2
        else:
            right = right / 2

        if right - left < 10:
            for i in range(left, right):
                if befind[i] == n:
                    print("Число n лежит под индексом", i)
                    finded = True
                
