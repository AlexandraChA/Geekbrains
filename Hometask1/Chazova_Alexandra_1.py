duration = int(input('Введите время в секундах: '))

if duration < 60:
    print(f'{duration} сек')
elif 60 <= duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(f'{minutes} мин {seconds} сек')
elif 3600 <= duration < 86400:
    seconds = duration % 60
    hours = duration // 3600
    minutes = (duration-hours*3600) // 60
    print(f'{hours} час {minutes} мин {seconds} сек')
elif duration < 0:
    print('Введите число больше 0.')
else:
    seconds = duration % 60
    days = duration // 86400
    hours = (duration-days*86400)//3600
    minutes = (duration - days*86400 -hours * 3600) // 60
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')