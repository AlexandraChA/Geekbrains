numbers = [number**3 for number in range(1,1001)]
#print(numbers)

#task 1
def sum_div_7(number_list):
    list_number1 = []
    for number in number_list:
        summ = 0
        number_sum = number
        while number_sum != 0:
            summ = summ + number_sum % 10
            number_sum = number_sum // 10
        if summ % 7 == 0:
            list_number1.append(number)
    result1 = sum(list_number1)
    return result1

print(sum_div_7(numbers))

#task2
new_numbers = [number+17 for number in numbers]
#print(new_numbers)
print(sum_div_7(new_numbers))

#task 3
numbers_3 = numbers[:]
for i in range(len(numbers_3)):
    numbers_3[i] = numbers_3[i] + 17
#print(numbers_3)
print(sum_div_7(numbers_3))
