data = ('ФИО', 'студент', 'телефон', 'институт', 'группа')


def create(data):
    full_name, student, telephone, institute, group = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Full_name: {} </p>\n' \
        .format(style, full_name)
    html += '    <p {}>Studen: {} </p>\n' \
        .format(style, student)
    html += '    <p {}>Telephone: {} </p>\n' \
        .format(style, telephone)
    html += '    <p {}>Institute: {} </p>\n' \
        .format(style, institute)
    html += '    <p {}>Group: {} </p>\n' \
        .format(style, group)
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html


print(create(data))