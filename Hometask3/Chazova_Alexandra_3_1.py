numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(num):
    if num in numbers:
        return numbers[num]
    else:
        return None

print(num_translate('one'))
print(num_translate('eleven'))