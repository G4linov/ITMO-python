def find_garbage_id(size_item, garbage_list):
    for i in range(len(garbage_list)):
        if (garbage_list[i] is not None) and (size_item == garbage_list[i][1]):
            return i
    return None

garbage = []
out_list = []

iron_len = 11700
index_order = 0


control = True
fix = None

while control:
    value = int(input("Введите количество эл: "))
    size = int(input("Введите размер эл: "))

    out_list.append([index_order + 1, 0, 0])

    i = 0
    for el in garbage:
        if (el is not None) and (value > out_list[index_order][1]) and (size <= el[1]):
            if el[1] % size == 0:
                if value == el[0] * (el[1] // size):
                    out_list[index_order][1] = el[0] * (el[1] // size)
                    el = None
                    garbage[i] = None
                    value = 0
                elif value > el[0] * (el[1] // size):
                    temp_size = el[1]
                    while el is not None:
                        el[1] -= size
                        out_list[index_order][1] += 1
                        if el[1] == 0:
                            el[0] -= 1
                            if el[0] == 0:
                                el = None
                                garbage[i] = None
                            else:
                                el[1] = temp_size
                else:
                    while out_list[index_order][1] != value:
                        new_el_len = el[1]
                        el[0] -= 1
                        while new_el_len != 0:
                            new_el_len -= size
                            out_list[index_order][1] += 1
                            if out_list[index_order][1] == value:
                                break
                        if new_el_len != 0:
                            id = find_garbage_id(new_el_len, garbage)
                            if id is not None:
                                garbage[id][0] += 1
                            else:
                                garbage.append([1,new_el_len])
            else:
                if value == el[0] * (el[1] // size):
                    out_list[index_order][1] = el[0] * (el[1] // size)

                    el[1] = round(el[1] % size, 1)

                    id = find_garbage_id(el[1], garbage)
                    if id is not None:
                        garbage[id][0] += el[0]
                        el = None
                        garbage[i] = None
                elif value > el[0] * (el[1] // size):
                    temp_el = el.copy()
                    while (el[0] > 0):
                        if el[1] - size > 0:
                            el[1] -= size
                            out_list[index_order][1] += 1
                        else:
                            el[0] -= 1
                            el[1] = temp_el[1]
                    id = find_garbage_id(round(temp_el[1] % size, 1), garbage)
                    if id is not None:
                        garbage[id][0] += temp_el[0]
                        el = None
                        garbage[i] = None
                    else:
                        el[0] = temp_el[0]
                        el[1] = round(temp_el[1] % size, 1)
                else:
                    while out_list[index_order][1] != value:
                        new_el_len = el[1]
                        if el[0] == 1:
                            while el[1] - size > 0:
                                el[1] -= size
                                out_list[index_order][1] += 1
                                if out_list[index_order][1] == value:
                                    break    
                        else:
                            el[0] -= 1
                            while new_el_len - size > 0:
                                new_el_len -= size
                                out_list[index_order][1] += 1
                                if out_list[index_order][1] == value:
                                    break                            
                            id = find_garbage_id(round(new_el_len, 1), garbage)
                            if id is not None:
                                garbage[id][0] += 1
                            else:
                                garbage.append([1, round(new_el_len, 1)])
        
        i += 1
    print(garbage)
    while (out_list[index_order][1] != value) and (value > 0):
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
    if quit_control == "ex":
        control = False

print(garbage)

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


"""
out_list = [[number_order, value_order, value_zagotovok]]
garbage = [[1, 6], [2, 2], [1, 3]]
value = 2 size = 3
-> garbage = [None, [2, 2], [1, 3]]
"""