from import_data import import_data
from export_data import export_data
from print_data import print_data

def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    id_num = input("Порядковый номер контакта: ")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите комментарий контакта: ")
    return [id_num, first_name, last_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    else:
        data = export_data()
        print_data(data)