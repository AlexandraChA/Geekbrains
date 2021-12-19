keys = []
values = []
count1 = 0
count2 = 0

with open('users.txt', 'r', encoding = 'utf-8') as file_1:
    for line in file_1:
        key_l = line.replace("\n", "")
        key_l = tuple(key_l.split(","))
        keys = keys + [key_l]
        count1 += 1

with open('hobby.txt', 'r', encoding= "utf-8") as file_2:
    for line in file_2:
        value_l = line.replace("\n", "")
        value_l = value_l.split(",")
        values = values + [value_l]
        count2 += 1
    if count1 > count2:
        for i in range(count1 - count2):
            values = values + [None]

#Выбрала списки, потому что список хобби может меняться. А кортеж для ФИО, так как список целиком не может быть ключом

diction = dict(zip(keys, values))

print(diction)
#{('Иванов', 'Иван', 'Иванович'): ['скалолазание', 'охота'], ('Петров', 'Петр', 'Петрович'): ['горные лыжи'], ('Петров', 'Сергей', 'Петрович'): None, ('Петров', 'Иван', 'Петрович'): None}