# Запросить информацию и показать информацию

def online_calc_massage():
    print('\nКалькулятор онлайн \n')


def choose_operation_massage():
    print('Выберите операцию')


def show_menu():
    menu = {
        1: 'Сложение',
        2: 'Деление',
        3: 'Возведение в степень',
        4: 'Умножение',
        5: 'Вычитание',
        6: 'Остаток от деления',
        7: 'Нахождение факториала',
        8: 'Логарифм числа',
        9: 'Возведение в квадрат',
        10: 'Возведение в куб',
        11: 'Нахождение квадрата числа'
    }
    return menu

def input_numberA(): #ввод первого числа    
    number_a = input('Число А: ')  
    if number_a.find('.') == True:
        number_a = float(number_a)
    else: number_a = int(number_a)
    return number_a

def input_numberB(): #ввод второго числа
    number_b = input('Число B: ')    
    if number_b.find('.') == True:
        number_b = float(number_b)
    else: number_b = int(number_b)
    return number_b

def printResult(x):    
    print(f'Результат : {x}\n')