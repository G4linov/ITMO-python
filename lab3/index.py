import random

def binarySearch(bi_list: list, left: int, right: int, dig: int):
    if left < right:
        mid = (left + right) // 2
        if (bi_list[mid] == dig):
            return mid
        elif (bi_list[mid] < dig):
            left = mid + 1
            return binarySearch(bi_list, left, right, dig)
        else:
            right = mid - 1
            return binarySearch(bi_list, left, right, dig)
    else:
        return None

def randList(k: int, n: int, m: int):
    rand_list = []
    for i in range(k):
        rand_list.append(random.randint(n, m))
    rand_list.sort()
    return rand_list

k = int(input("Введите размер массива: "))
n = int(input("Введите первое число диапозона: "))
m = int(input("Введите второе число диапозона: "))
j = int(input("Введите искомое число: "))

if n > m:
    find_arr = randList(k, m, n)
else:
    find_arr = randList(k, n, m)

right = len(find_arr)
left = 0

x = binarySearch(find_arr, left, right, j)

if (x == None):
    print("числа", j, "нет в списке")
else:
    print("Число:", j, "находится под индексом:", x)