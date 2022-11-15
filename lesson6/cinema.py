# Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді
# форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...). Наприклад :



#list, containing exceptions to be used when looking for correct word form.




def age_input():
    '''
    Simple function to receive user age input
    Returns:str

    '''
    age = (input('Введіть Ваш вік цифрами: '))
    return age


input_data = age_input()


def years_form(user_data=input_data):
    '''
    A function that chooses correct form of 'роки' word.
    Args:
        user_data(str): received from variable, which stores previous function - user input.

    Returns:
        str of correct word form of 'роки' word
    '''
    teens = ['11', '12', '13', '14', '15', '16', '17', '18', '19',
             '111', '112', '113', '114', '115', '116', '117', '118', '119']
    if user_data in teens:
        years = 'років'
    elif user_data.endswith('1'):
        years = 'рік'
    elif user_data.endswith(('2','3','4')):
        years = 'роки'
    else:
        years = 'років'
    return years





def looking_for_seven(entry=input_data):
    '''
    Simple function which iterates for '7' digit in user age
    Args:
        entry(str): uses users age, stored in a variable

    Returns:
            bool True if found the '7' digit.
    '''
    seven = False
    for char in entry:
        if char == '7':
            seven = True
        else:
            seven = False
    return seven





def age_int(user_age=input_data):
    '''
    A simple function to check if entered data can be converted to int value'
    Args:
        user_age(str): uses user input

    Returns:
        int value of user input or an Error when data is invalid.
    '''
    try:
        integer_age = int(user_age)
        return integer_age
    except Exception as e:
        print('Помилка. Введені дані не є віком.')




def final_answer():
    '''
    The final fortune wheel. Assigns the comment added to collected data. Uses data returned by
    previous functions and stored in variables.
    Returns:
    str containing cashiers response.
    '''
    user_age_int = age_int()
    seven_found = looking_for_seven()
    years_form_value = years_form()
    answer = ''
    try:
        if 0 < user_age_int < 122 and seven_found:
            answer = f'Вам {user_age_int} {years_form_value}. Вам пощастить!'
        elif user_age_int == 0:
            answer = 'А так буває?'
        elif user_age_int > 122:
            answer = 'Найстаріша людина в історії прожила 122 роки. А ви, певно, ще й динозаврів пам‘ятаєте? :)'
        elif user_age_int < 7:
            answer = f'Тобі ж {user_age_int} {years_form_value}! Де твої батьки?'
        # elif user_age_int in (11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 122):
        #     answer = 'Як цікаво!'
        ### Rudiment of a previous homework, but might as well be used as another case of validation.
        elif user_age_int < 16:
            answer = f'Тобі лише {user_age_int} {years_form_value}! А це фільм для дорослих!'
        elif user_age_int > 65:
            answer = f'Вам {user_age_int} {years_form_value}? Покажіть пенсійне посвідчення!'
        else:
            answer = f'Не зважаючи на те, що Вам {user_age_int} {years_form_value}, білетів вже немає!'
        return answer
    except:
        return 'Будь ласка, спробуйте ще раз.'
        pass



print(final_answer())
