def thesaurus_adv(*names):
    dict = {} #let:name
    dict_l = {}
    for name in names:
        let = name[0]
        if let not in dict:
            dict[let] = []
            dict[let].append(name)
        else:
            dict[let].append(name)
    for key in dict.keys():
        list_n= dict[key]
        for name in list_n:
            name_s = name.split()
            let_2 = name_s[1][0]
            if let_2 not in dict_l:
                dict_l[let_2] = []
                dict_l[let_2].append(name)
            else:
                dict_l[let_2].append(name)
        dict[key] = dict_l
        dict_l = {}

    return dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))