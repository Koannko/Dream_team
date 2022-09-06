def user_data():
    """Функция формирования данных из текстовых файлов"""
    name_dict = []
    name_key = ['статус', 'телефон', 'факультет', 'группа']
    name_typle = {}
    with open("Students.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line_dict = line.strip("\n").split(',')
            if line_dict[-1] == '':
                line_dict.pop()
                name_dict.append(line_dict)
            else:
                name_dict.append(line_dict)
    for i in range(0, len(name_dict)):
        inform = {name_key[j]: name_dict[i][j + 1] for j in range(0, len(name_key))}
        name_typle[name_dict[i][0]] = inform
    return name_typle


def information_name(fun, name, status):
    return print(fun[name][status])


information_name(user_data(), 'Иванова Полина Павловна', 'статус')


def information_name(fun, name, number):
    return print(fun[name][number])


information_name(user_data(), 'Иванова Полина Павловна', 'телефон')


def information_name(fun, name, group):
    return print(fun[name][group])


information_name(user_data(), 'Иванова Полина Павловна', 'группа')