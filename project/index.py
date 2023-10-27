def find_garbage_id(item, garbage_list):
    for i in range(len(garbage_list)):
        if (garbage_list[i][0] != -1 ) and (garbage_list[i][1] == item):
            return i
    return None

def add_new_garbage(item, garbage_list):
    id = find_garbage_id(round(item[1], 1), garbage_list)
    if id is not None:
        garbage_list[id][0] += item[0]
    else:
        garbage_list.append(item)
    return garbage_list

garbage = []
out_list = []

iron_len = 11700
index_order = 0

control = True

while control:
    value = int(input("Введите количество эл: "))
    size = int(input("Введите размер эл: "))

    out_list.append([index_order + 1, 0, 0])

    for el in garbage:
        if value >= el[0] * (el[1] // size):
            temp_el = el.copy()
            while el[0] >= 1:
                while el[1] - size > 0:
                    out_list[index_order][1] += 1
                    el[1] -= size
                if el[0] == 1 and el[0] == 0:
                    el[0], el[1] = -1, -1
                    break
                elif el[0] == 1:
                    el[0] = round(temp_el[0], 1)
                    break
                else:
                    el[0] -= 1
                    el[1] = temp_el[1]
        else:
            new_gabage_el = [0, 0]
            temp_el = el.copy()
            while el[1] - size > 0:
                out_list[index_order][1] += 1
                el[1] -= size
                if el[1] - size < 0 and new_gabage_el[0] == 0:
                    new_gabage_el[0] = 1
                    new_gabage_el[1] = el[1]
                    el[0] -= 1
                    el[1] = temp_el[1]
                elif el[1] - size < 0:
                    new_gabage_el[0] += 1
                    el[0] -= 1
                    el[1] = temp_el[1]
                if out_list[index_order][1] == value:
                    break

    
    while (out_list[index_order][1] != value):
        temp_iron_len = iron_len
        out_list[index_order][2] += 1
        while temp_iron_len - size > 0:
            temp_iron_len -= size
            out_list[index_order][1] += 1
            if out_list[index_order][1] == value:
                break
        if round(temp_iron_len, 1) != 0:
            id = find_garbage_id(round(temp_iron_len, 1), garbage)
            if id is not None:
                garbage[id][0] += 1
            else:
                garbage.append([1, round(temp_iron_len, 1)])
            
    index_order += 1

    quit_control = input("Для выхода введите 0: ")
    if quit_control == "0":
        control = False                

value_iron = 0
for el in out_list:
    value_iron += el[2]
print("Всего новых железяк:", value_iron)

for el in out_list:
    print("Для заказа №", el[0], "потребуется новых железяк:", el[2])

print("Элементы не использованные:")
for el in garbage:
    if el is not None:
        print("Колчиство:", el[0], "длиной:", el[1])