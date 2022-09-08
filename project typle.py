def user_data():
    """Функция формирования данных студентов из текстового файла"""
    file_user = []
    name_key = ['ФИО', 'статус', 'пароль', 'телефон', 'факультет', 'группа']
    base_user = []
    with open("Students.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line_dict = line.strip("\n").strip('.').split(',')
            file_user.append(line_dict)
    for i in range(0, len(file_user)):
        inform = {name_key[j]: file_user[i][j] for j in range(0, len(name_key))}
        base_user.append(inform)
    return base_user


def teachers_data():
    """Функция формирования данных преподавателей из текстового файла"""
    file_teacher = []
    name_key = ['ФИО', 'статус', 'пароль', 'почта', 'институт', 'кафедра']
    base_teacher = []
    with open("Teachers.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line_dict = line.strip("\n").strip('.').split(',')
            file_teacher.append(line_dict)
    for i in range(0, len(file_teacher)):
        inform = {name_key[j]: file_teacher[i][j] for j in range(0, len(name_key))}
        base_teacher.append(inform)
    return base_teacher


def data_entry(base):
    """Рекурсивная функция проверки ввода имени и пароля"""
    user_name = input('Введите своё ФИО: ')
    user_pass = input('Введите свой пароль: ')
    stat = verification(base, user_name, user_pass)
    if stat != 0:
        return stat
    else:
        data_entry(base)


def verification(base, name, password):
    """Функция для авторизации пользователя"""
    for i in range(len(base)):
        if base[i]['ФИО'] == name:
            if base[i]['пароль'] == str(password):
                if base[i]['статус'] == 'ученик':
                    print('Вы авторизованы как ученик.')
                    return 'ученик'
                else:
                    print('Вы авторизованы как учитель.')
                    return 'учитель'
            else:
                print('Неверный логин или пароль.')
                return 0


def information_people(base, name, inform):
    """Функция для выдачи запрашиваемой информации"""
    for i in range(len(base)):
        if base[i]['ФИО'] == name:
            return f'{base[i]["ФИО"]}: {inform} {base[i][inform]}'
        else:
            return f'{inform} с таким именем не найден.'


def request_verification(base, name, info):
    """Функция выдачи информации, в зависимости от статуса"""
    return 1
    # for i range(len(base)):
    #     if base[i]['ФИО'] == name:
    #         pass
    # if checking_status(base, name, status) == 1
    #     pass


def checking_status (base, name, status):
    """Функция проверки статуса"""
    for i in range(len(base)):
        if base[i][name] == name:
            if base[i][status] == 'ученик':
                return 1
            else:
                return 2


students = user_data()  # достаточно сформировать базу один раз, затем ею пользоваться
teachers = teachers_data()
# print(students)
# print(information_people(teachers, 'Тюрина Зоя Владимировна', 'статус'))
# print(information_people(teachers, 'Акимова Мария Артемьевна', 'почта'))
# print(information_people(students, 'Аникин Александр Никитич', 'факультет'))

status = data_entry(students + teachers)
print(status)





