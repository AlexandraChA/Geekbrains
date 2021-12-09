def thesaurus(*names):
    dict = {} #let:name
    for name in names:
        let = name[0]
        if let not in dict:
            dict[let] = []
            dict[let].append(name)
        else:
            dict[let].append(name)
    return dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

def sort_dict(dict):
    list_let = list(dict.keys())
    list_let.sort()
    for i in list_let:
        print(f'{i}: {dict[i]}')

sort_dict(thesaurus("Иван", "Мария", "Петр", "Илья"))