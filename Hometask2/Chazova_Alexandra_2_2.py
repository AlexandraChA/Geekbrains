list_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(list_words))
new_list = []
def only_sign(x):
    if x[0] in '+-':
        return x[0]

for i in range(len(list_words)):
    sign = only_sign(list_words[i])
    if (list_words[i].isdigit()) or((sign !=None) and (list_words[i][1:].isdigit())):
        new_list.append('"')
        if (sign != None):
            if int(list_words[i][1:]) < 10:
                new_list.append(f'{sign}0{list_words[i][1:]}')
            else:
                new_list.append(list_words[i])
        else:
            if int(list_words[i]) < 10:
                new_list.append(f'0{list_words[i]}')
            else:
                new_list.append(list_words[i])
        new_list.append('"')
    else:
        new_list.append(list_words[i])

print(new_list)
print(id(new_list))
print(' '.join(new_list))