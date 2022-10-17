# Мозг (Александр)

from calculator.models.model_addition import fn_addition #сложение
from calculator.models.model_division import fn_division #деление
from calculator.models.model_exponentiation import fn_model_exponentiation #возведение в степень
from calculator.models.model_factorial import fn_model_factorial #факториал
from calculator.models.model_logarifm import fn_model_logarifm #логарифм
from calculator.models.model_multiplication import fn_model_multiplication #умнижение
from calculator.models.model_remainder_division import fn_model_remaider_division #остаток от деления
from calculator.models.model_second_degree import fn_model_second_degree #квадрат числа
from calculator.models.model_subtraction import fn_model_subtraction #вычитание
from calculator.models.model_third_degreee import fn_model_third_degree #куб числа
from calculator.models.model_sqrt import fn_model_sqrt #квадратный корень из числа 
import view
import errors

def select_menu(a):
    if a == 1:
        fn_addition(view.input_numberA(), view.input_numberB())
    if a == 2:
        fn_division(view.input_numberA(), view.input_numberB())
    if a == 3:
        fn_model_exponentiation(view.input_numberA(), view.input_numberB())
    if a == 4:
        fn_model_multiplication(view.input_numberA(), view.input_numberB())
    if a == 5:
        fn_model_subtraction(view.input_numberA(), view.input_numberB())
    if a == 6:
        fn_model_remaider_division(view.input_numberA(), view.input_numberB())
    if a == 7:
        fn_model_factorial(view.input_numberA())
    if a == 8:
        fn_model_logarifm(view.input_numberA(), view.input_numberB())
    if a == 9:
        fn_model_second_degree(view.input_numberA())
    if a == 10:
        fn_model_third_degree(view.input_numberA())
    if a == 11:
        fn_model_sqrt(view.input_numberA())
    if  (a > 11 or a < 1):
        errors.errorMenuChoose()