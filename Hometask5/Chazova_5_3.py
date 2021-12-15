tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Serega'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б',
]

def name_class():
    i=0
    j=0
    while i !=len(tutors):
        if len(tutors) <= len(klasses):
            yield (tutors[i], klasses[j])
            i += 1
            j += 1
        else:
            if i >= len(klasses):
                yield (tutors[i], None)
            else:
                yield (tutors[i], klasses[j])
            i += 1
            j += 1



for gen in name_class():
    print(gen)
