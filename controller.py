from model.fun_teachers import *
from model.fun_students import *
from model.project_typle import *
from view.html_creater import *
from model.new_user import *
from model.users_request import *


def start():
    students = users_data()
    teachers = teachers_data()
    base = students + teachers
    value_sign = data_entry(base)

    if value_sign == 1:
        data_new = get_value()
        while not checking_emptiness(data_new):
            data_new = get_value()
        new_user(data_new)
        return 0
    user_fio, status = value_sign
    surname, name, patr = user_fio.split(' ')
    users_request(students, teachers, status)
    return 0


start()
