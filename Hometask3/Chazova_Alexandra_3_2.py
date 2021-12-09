numbers = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(num):
    if num.lower() in numbers:
        if num.istitle():
            return numbers[num.lower()].title()
        else:
            return numbers[num]
    else:
        return None

print(num_translate('one'))
print(num_translate('One'))
print(num_translate('eleven'))