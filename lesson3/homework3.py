    #1.
    # Напишіть код, який сформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад
    # "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та
    # номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python"
    # а номер символу 3) - "The 3 symbol in 'Python' is 't' ".

word = input('Enter a single word: ')
while not word.isalpha():
    print('Oops! The data you entered is not a single word.')
    break
while word.isalpha():
    symb_input = input(f'Enter the symbol number in range of 1 to {len(word)}: ')

    if not symb_input.isdigit():
        print('Oops! The data you entered is not a valid symbol number.')
    else:
        symb = int(symb_input)
        while symb > 0 and symb < (len(word)+1):
            print(f'The {symb} symbol in \'{word}\' is \'{word[symb-1]}\'')
            break
        else:
            print('Oops! Wrong symbol number.')
        break
    break


# 2.
    # Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
#     Напишіть код, який визначить кількість слів, в цих даних.

#Моє перше рішення:
# text = input('Введіть текст: ')
# split_text = text.split()
# words_only_list = [item for item in split_text if item.isalpha()]
#
# if words_only_list:
#     print(f'Кількість слів у введеному тексті дорівнює {len(words_only_list)}.')
# else:
#     print('Помилка. Схоже, у введеному тексті немає слів.')
# На жаль, даний код не працює у випадку наявності пунктуаційних знаків.

text = str(input('Введіть текст: '))
counter = text.count(' ')

print(f'Кількість слів у вашому тексті дорівнює {counter+1}.'
      f'\nПримітка! Словами вважаються будь-які дані, розділені пробілом!')

# 3.
    # Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
    # Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float),
    # які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

list_1 = ['1', '2', 3, True, 'False', 5.5, '6', 7, 8, 'Python', 9, 0.1, 'Lorem Ipsum']
list_2 = [number for number in list_1 if type(number) is int or type(number) is float]

print(f'Ваш список: {list_1}')
print(f'Виключно дані типів \'int\' та \'float\' з Вашого списку: {list_2}')