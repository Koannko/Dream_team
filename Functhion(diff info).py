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


def information_status(fun, name, status):
    return print(fun[name][status])


information_status(user_data(), 'Иванова Полина Павловна', 'статус')


def information_number(fun, name, number):
    return print(fun[name][number])


information_number(user_data(), 'Иванова Полина Павловна', 'телефон')


def information_faculty(fun, name, faculty):
    return print(fun[name][faculty])


information_faculty(user_data(), 'Иванова Полина Павловна', 'факультет')


def information_group(fun, name, group):
    return print(fun[name][group])


information_group(user_data(), 'Иванова Полина Павловна', 'группа')