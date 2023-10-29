garbage = []
out_list = []

iron_len = 11700
index_order = 0

while True:
    value = int(input("Введите количество эл: "))
    size = int(input("Введите размер эл: "))

    out_list.append([index_order + 1, 0, 0])

    index = 0
    list_of_indexes = []
    for el in garbage:
        if (el - size) >= 0 and (out_list[index_order][1] != value):
            if (el - size) == 0:
                list_of_indexes.append(index)
                out_list[index_order][1] += 1
            else:
                el -= size
                out_list[index_order][1] += 1
        elif out_list[index_order][1] == value:
            break
        index += 1
    
    for ind in list_of_indexes:
        garbage[ind] = 0

    while 0 in garbage:
        garbage.remove(0)

    while (out_list[index_order][1] != value):
        temp_iron_len = iron_len
        out_list[index_order][2] += 1
        while temp_iron_len - size > 0:
            temp_iron_len -= size
            out_list[index_order][1] += 1
            if out_list[index_order][1] == value:
                break
        garbage.append(temp_iron_len)
            
    index_order += 1

    quit_control = input("Для выхода введите 0: ")
    if quit_control == "0":
        break              

value_iron = 0
for el in out_list:
    value_iron += el[2]
print("Всего новых железяк:", value_iron)

for el in out_list:
    print("Для заказа №", el[0], "потребуется новых железяк:", el[2])
 
sum_garbage = 0
for el in garbage:
    sum_garbage += el

print("Итоговоая длина мусора:", sum_garbage)