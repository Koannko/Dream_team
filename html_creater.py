# Выводит данные студента на страницу
def create_student(data_view):
    if (data_view):
        Patronymic, student, password, telephone, faculty, group = data_view
        style = 'style="font-size:30px;"'
        html = '<html>\n  <head><meta charset="UTF-8"></head>\n  <body>\n'
        html += '    <p {}>Patronymic: {} </p>\n' \
            .format(style, Patronymic)
        html += '    <p {}>student: {} </p>\n' \
            .format(style, student)
        html += '    <p {}>password: {} </p>\n' \
            .format(style, password)
        html += '    <p {}>telephone: {} </p>\n' \
            .format(style, telephone)
        html += '    <p {}>faculty: {} </p>\n' \
            .format(style, faculty)
        html += '    <p {}>group: {} </p>\n' \
            .format(style, group)
        html += '  </body>\n</html>'

        with open('index.html', 'w', encoding="utf-8") as page:
            page.write(html)
            page.close()
        return html

# Выводит данные учителя на страницу
def create_teacher(data_view):
    if (data_view):
        Patronymic, teacher, password, mail, institute, department = data_view
        style = 'style="font-size:30px;"'
        html = '<html>\n  <head><meta charset="UTF-8"></head>\n  <body>\n'
        html += '    <p {}>Patronymic: {} </p>\n' \
            .format(style, Patronymic)
        html += '    <p {}>teacher: {} </p>\n' \
            .format(style, teacher)
        html += '    <p {}>password: {} </p>\n' \
            .format(style, password)
        html += '    <p {}>mail: {} </p>\n' \
            .format(style, mail)
        html += '    <p {}>institute: {} </p>\n' \
            .format(style, institute)
        html += '    <p {}>department: {} </p>\n' \
            .format(style, department)
        html += '  </body>\n</html>'

        with open('index.html', 'w', encoding="utf-8") as page:
            page.write(html)
            page.close()
        return html

# Регистрация
def get_value():
    print('Регистрация')
    my_list = []
    Patronymic = input('Введите ФИО ')
    status = input ('Введите статус: учитель или ученик ')
    password = input('Введите пароль ')
    if (status == 'учитель'):
        mail = input('Введите почту ')
        institute = input('Введите институт ')
        department = input('Введите кафедру ')
        my_list.append(Patronymic)
        my_list.append('учитель' )
        my_list.append(password)
        my_list.append(mail)
        my_list.append(institute)
        my_list.append(department)
        return my_list
    else:
        telephone = input('Введите телефон ')
        faculty = input('Введите факультет ')
        group = input('Введите группа ')
        my_list.append(Patronymic)
        my_list.append('ученик' )
        my_list.append(password)
        my_list.append(telephone)
        my_list.append(faculty)
        my_list.append(group)
        return my_list

value_registration = get_value()

# Проверка формы регистра на пустоту
def checking_emptiness(value_registration):
    if (not value_registration[0] or not value_registration[1] or not value_registration[2]):
        return 0
    else:
        return 1
print(checking_emptiness(value_registration))
# Найти пользователя
def search_user():
    print('Наити')
    my_list = []
    Patronymic = input('Введите ФИО ')
    status = input ('Введите статус: учитель или ученик ')
    my_list.append(Patronymic)
    my_list.append(status )
    my_str = (" ".join(my_list))
    return my_str


