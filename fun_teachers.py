def teachers_data():
    """Функция формирования данных из текстовых файлов"""
    name_dict = []
    name_key = ['статус', 'почта', 'институт', 'кафедра']
    name_typle = {}
    with open("Teachers.txt", "r", encoding="utf-8") as f:
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



def information_status_teacher(fun, name, status):
    return print(fun[name][status])


information_status_teacher(teachers_data(), 'Тюрина Зоя Владимировна', 'статус')


def information_mail(fun, name, mail):
    return print(fun[name][mail])


information_mail(teachers_data(), 'Тюрина Зоя Владимировна', 'почта')


def information_college(fun, name, college):
    return print(fun[name][college])


information_college(teachers_data(), 'Тюрина Зоя Владимировна', 'институт')


def information_department(fun, name, department):
    return print(fun[name][department])


information_department(teachers_data(), 'Тюрина Зоя Владимировна', 'кафедра')