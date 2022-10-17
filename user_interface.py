# Мозг
import model_addition as ma


def select_menu(a):
    if a == 1:
        number_a = int(input('Число А: '))
        number_b = int(input('Число Б: '))
        ma.fn_addition(number_a, number_b)
