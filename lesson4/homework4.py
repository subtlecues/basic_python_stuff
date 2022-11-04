# Дана довільна строка. Напишіть код, який знайде в ній і виведе на екран кількість слів, які містять
# дві голосні літери підряд.

text = str(input('Enter your text here to look for words with two vowels in a row: '))
text = text.lower()
text = text.split()
vowels = 'aeiou'
vowels_counter = 0
needed_words = 0
for word in text:
    vowels_counter = 0
    for letter in word:
        if letter in vowels:
            vowels_counter += 1
            if vowels_counter == 2:
                vowels_counter = 0
                needed_words += 1
                print(f'Word found! \'{word}\'')
                break
        elif letter not in vowels:
            vowels_counter = 0


print(f'The number of words with two vowels in a row is {needed_words}. '
      f'\n\nPlease note, that \'y\' letter is excluded from vowels list due to its occasional role as consonant.')
# TEST CASE: beetroot word was a great example of a test case to break my code.


# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:


my_dict = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

values = my_dict.values()
keys = my_dict.keys()
while True:

    try:
        lower_limit = float(input('Введіть нижню межу вартості: '))
        upper_limit = float(input('Введіть верхню межу вартості: '))

        print('За Вашим запитом знайдено: ')
        for value in values:
            if lower_limit <= value <= upper_limit:
                print(list(keys)
                      [list(values).index(value)])
        break
    except ValueError:
        print('Невірно введені дані.')
