def users_data():
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
        inform = {name_key[j]: name_dict[i][j + 1]
                  for j in range(0, len(name_key))}
        name_typle[name_dict[i][0]] = inform
    return name_typle


def information_status(fun, name, status):
    return (fun[name][status])


def information_number(fun, name, number):
    return (fun[name][number])


def information_faculty(fun, name, faculty):
    return (fun[name][faculty])


def information_group(fun, name, group):
    return (fun[name][group])
