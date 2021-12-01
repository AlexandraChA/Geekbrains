#сразу же сделала без создания нового списка
list_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(list_words))
def only_sign(x):
    if x[0] in '+-':
        return x[0]

i=0
while i < len(list_words):
    sign = only_sign(list_words[i])
    if (list_words[i].isdigit()) or ((sign !=None) and (list_words[i][1:].isdigit())):
        if (sign != None) and (int(list_words[i][1:]) < 10):
            list_words[i] = f'{sign}0{list_words[i][1:]}'
        elif (sign == None) and (int(list_words[i])<10):
            list_words[i] = f'0{list_words[i]}'
        list_words.insert(i, '"')
        list_words.insert(i+2, '"')
        i += 2
    i += 1

print(list_words)
print(id(list_words))
print(' '.join(list_words))
