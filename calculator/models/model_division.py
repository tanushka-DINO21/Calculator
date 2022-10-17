# Деление

import errors
import view as view

def fn_division(a, b):
    if b == 0:
        errors.errorDisionZerro()
    else: return view.printResult(a // b)