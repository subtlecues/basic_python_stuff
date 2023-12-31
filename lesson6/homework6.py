#Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

def floating_numbers(user_input):
    '''
    A function which turns arg into float or returns '0' string otherwise.
    Args:
        user_input: a value of any type for function analysis.

    Returns:
        float value when available, '0' string otherwise.
    '''
    try:
        func_output = float(user_input)
        print(func_output)
        return func_output
    except Exception as e:
        print(0)
        return 0
#
#
# #Test cases
# floating_numbers(5)
# floating_numbers('blabla')
# floating_numbers(160*327)
# floating_numbers('!@#$%^&*()')

## #Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів


def second_func(arg1, arg2):
    '''
    A function which multiplies given args whe possible, otherwise returns a tuple with given args.
    Args:
        arg1: a data of any value
        arg2: a data of any value

    Returns:
        either an int result of a multiplication or a tuple, containing args.
    '''
    tuple_args = (arg1, arg2)
    try:
        if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
            return print(arg1*arg2)
        elif isinstance(arg1, str) and isinstance(arg2, str):
            return print(arg1 + arg2)
        else:
            return print(tuple_args)
    except TypeError:
        return print(tuple_args)

# TEST CASES
# second_func(['6'], 6)
# print('list and int')
# second_func(7, 2)
# print('numbers')
# second_func('blabla', ' and another blabla')
# print('strings')
# second_func(None, False)
# print('bool and None')
# second_func(1, 'string')
# print('int and string')
# second_func('None', False)
# print('string and bool')
# second_func('6',6)
# print('string and int')

