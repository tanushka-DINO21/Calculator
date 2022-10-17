# кнопка запуска

import view as view
import user_interface as ui

exit()

view.online_calc_massage()
view.choose_operation_massage()

for key in view.show_menu():
    print(f' - {key} - {view.show_menu()[key]}')


def do():
    button = int(input('Введите номер операции: '))

    ui.select_menu(button)

    print('\nДля продолжения введите 0')

    a = int(input())

    if a == 0:
        do()
    else: exit()
