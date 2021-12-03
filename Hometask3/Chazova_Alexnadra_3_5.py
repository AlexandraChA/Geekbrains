from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    jokes = []
    for i in range(0, n):
        first_word = choice(nouns)
        second_word =choice(adverbs)
        third_word = choice(adjectives)
        first_joke = [first_word, second_word, third_word]
        first_joke = ' '.join(first_joke)
        jokes.append(first_joke)
    return jokes

print(get_jokes(2))