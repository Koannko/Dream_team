# Выводит данные пользователя на страницу
def create(data_view):
    if (data_view):
        Surname, Name, Patronymic, password = data_view
        style = 'style="font-size:30px;"'
        html = '<html>\n  <head><meta charset="UTF-8"></head>\n  <body>\n'
        html += '    <p {}>Surname: {} </p>\n' \
            .format(style, Surname)
        html += '    <p {}>Name: {} </p>\n' \
            .format(style, Name)
        html += '    <p {}>Patronymic: {} </p>\n' \
            .format(style, Patronymic)
        html += '    <p {}>password: {} </p>\n' \
            .format(style, password)
        html += '  </body>\n</html>'

        with open('index.html', 'w', encoding="utf-8") as page:
            page.write(html)
            page.close()
        return html


def get_value(errors=0):
    print('Регистрация')
    my_list = []
    Surname = input('Введите свою фамилию ')
    Name = input('Введите свое имя ')
    Patronymic = input('Введите свое отчество ')
    password = input('Введите пароль ')
    my_list.append(Surname)
    my_list.append(Name)
    my_list.append(Patronymic)
    my_list.append(password)
    return my_list
