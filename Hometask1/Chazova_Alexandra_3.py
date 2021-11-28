for i in range(1,101):
    if (i % 10 == 1) and (i != 11):
        print(f'{i} процент')
    elif ((i % 10 == 2) or (i %10 ==3) or (i%10==4)) and (i != 12) and (i!=13) and (i!=14):
        print(f'{i} процента')
    else:
        print(f'{i} процентов')