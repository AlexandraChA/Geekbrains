prices = [55.25, 49.07, 98, 125.11, 32.03, 88.2, 190, 22.63, 49.4, 63, 28.51]
def get_prices(prices):
    list_prices = []
    for i in prices:
        rubles = int(i // 1)
        kop = int((i % 1) * 100)
        if kop < 10:
            kop = f'0{kop}'
        list_prices.append(f'{rubles} руб {kop} коп')
    return list_prices

#1 Вывести цены в виде руб коп
print(', '.join(get_prices(prices)))
print(id(prices))

#2 Отсортировать список по возрастанию
prices.sort()
print(id(prices))
print(', '.join(get_prices(prices)))

#3 Новый список, отсортированный по убыванию
new_prices = sorted(prices, reverse= True)
print(id(new_prices))
print(', '.join(get_prices(new_prices)))

#4 Вывести цены 5 самых дорогих продуктов
print(f"Цены пяти самых дорогих товаров: {', '.join(get_prices(new_prices)[0:5])}")