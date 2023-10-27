def add(table: dict, value):
    c = []
    if table.get(hash(value)) == None:
        c.append(value)
        table[hash(value)] = c
    else:
        table.get(hash(value)).append(value)

def remove(table: dict, value):
    if table.get(hash(value)) == None:
        return "Not found key for this value"
    else:
        if value in table.get(hash(value)):
            table.get(hash(value)).remove(value)
            return "Remove complete"
        else:
            return "Not found value"

def search(table: dict, value):
    if table.get(hash(value)) == None:
        return "Not found value"
    else:
        if value in table.get(hash(value)):
            return value
        else:
            return "Not found value"

hash_table = {}
while(True):
  data_raw = input("Pleace enter value: ")

  if(data_raw == "add"):
    value = input("Pleace enter value for insert into hash-table: ")
    if value.isdigit():
        value = int(value)
    add(hash_table, value)

  if(data_raw == "remove"):
    value = input("Pleace value for delete from hash-table: ")
    if value.isdigit():
        value = int(value)
    print(remove(hash_table, value))

  if(data_raw == "search"):
    value = input("Pleace value for search from hash-table: ")
    if value.isdigit():
        value = int(value)
    print(search(hash_table, value))

  if(data_raw == "print"):
    print(hash_table)
