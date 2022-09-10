from fun_teachers import *
from fun_students import *
from project_typle import *
from html_creater import *


def start():
    students = users_data()
    teachers = teachers_data()
    base = students + teachers
    value_sign = data_entry(base)
    print(value_sign)

    if value_sign == 1:
        data_new = get_value()
        print(data_new)

    else:
        user_fio, user_pass, status = value_sign
        surname, name, patr = user_fio.split(' ')
        data_view = surname, name, patr, '********'
        create(data_view)


start()

# Павел: добавить в регистрацию вопрос "Ученик или учитель?". Дальнейшие поля выстроить по базе данных. Функция возвращает список
# Проверка строки на пустоту: если пустая - 0, если все ок, то 1

# Лев, Елена. Функция сохраняет данные нового пользователя. На вход: список с данными как в базе данных. На выход список
