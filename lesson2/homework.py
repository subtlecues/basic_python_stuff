# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#
#
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
#
# - якщо користувачу менше 7 - вивести повідомлення "Де твої батьки?"
#
# - якщо користувачу менше 16 - вивести повідомлення  "Це фільм для дорослих!"
#
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
#
# - якщо вік користувача з двох однакових цифр - вивести повідомлення  "Як цікаво!"
#
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
#
#
# P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача з двох однакових цифр то має бути виведено тільки відповідне повідомлення! Також подумайте над варіантами, коли введені невірні або неадекватні дані.


age_input = input('Введіть Ваш повний вік цифрами: ')

if not age_input.isdigit():
    print('Досить бавитися!')
else:

    age = int(age_input)
    if age == 0:
        print('А так буває?')
    elif age > 122:
        print('Найстаріша людина в історії прожила 122 роки. А ви, певно, ще й динозаврів пам‘ятаєте? :)')
    elif age < 7:
        print('Де твої батьки?')
    elif age in (11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 122):
        print('Як цікаво!')
    elif age < 16:
        print('Це фільм для дорослих!')
    elif age > 65:
        print('Покажіть пенсійне посвідчення!')
    else:
        print('А білетів вже немає!')