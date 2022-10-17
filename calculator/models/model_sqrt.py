#нахождение квадратного корня из числа

import view
import math
import errors

def fn_model_sqrt(a):
    if a < 0:
       return errors.errorSwrtMinus()
    else: return view.printResult(math.sqrt(a))