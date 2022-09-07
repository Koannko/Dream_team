form_data = 'C:\\OpenServer\\domains\\shape\\mes.txt'

def create(data_view):
    Surname, Name, Patronymic = data_view
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Surname: {} </p>\n' \
        .format(style, Surname)
    html += '    <p {}>Name: {} </p>\n' \
        .format(style, Name)
    html += '    <p {}>Name: {} </p>\n' \
        .format(style, Patronymic)
    html += '    <p {}>Patronymic: {} </p>\n'
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html

def get_file(form_data):
    with open(form_data, 'r', encoding="utf-8") as data:
        my_tuple = data.read()
        my_tuple = tuple(map(str, my_tuple.split()))
        data.close()
        return my_tuple

data_view = get_file(form_data)

print(create(data_view))


def create_shape():
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '<form action="action.php" method="post">\n'
    html += '    <p>Surname: <input type="text" name="Surname" /></p>\n'
    html += '    <p>Name: <input type="text" name="Name" /></p>\n'
    html += '    <p>Patronymic: <input type="text" name="Patronymic" /></p>\n'
    html += '    <p><input type="submit" name="auth" value="Отправить" /></p>\n'
    html += '  </form>\n</body>\n</html>'

    with open('index.php', 'w') as page:
        page.write(html)

    return html

print(create_shape())