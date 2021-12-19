keys = []
values = []
count1 = 0
count2 = 0

with open('users.txt', 'r', encoding = 'utf-8') as file_1:
    for line in file_1:
        keys = keys + [line.replace("\n", "")]
        count1 += 1

with open('hobby.txt', 'r', encoding= "utf-8") as file_2:
    for line in file_2:
        values = values + [line.replace("\n","")]
        count2 += 1
    if count1 > count2:
        for i in range(count1 - count2):
            values = values + [None]

diction = dict(zip(keys, values))

print(diction)

#{'Иванов,Иван,Иванович': 'скалолазание,охота', 'Петров,Петр,Петрович': 'горные лыжи'}
#{'Иванов,Иван,Иванович': 'скалолазание,охота', 'Петров,Петр,Петрович': 'горные лыжи', 'Петров,Сергей,Петрович': None, 'Петров,Иван,Петрович': None}