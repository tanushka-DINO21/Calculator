# кнопка запуска

import view
import user_interface as ui

view.online_calc_massage()
view.choose_operation_massage()

for key in view.show_menu():
    print(f' - {key} - {view.show_menu()[key]}')

button = int(input('Введите номер операции: '))

ui.select_menu(button)
