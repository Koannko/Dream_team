def users_request(students, teachers, status):
    if status == 2:  # необходимо заменить учитель на статус, который получается при проверке статуса
        info_teacher = int(input(
            'Какая информация Вас интересует: 1 - данные студентов, 2 - данные преподавателей:\n'))
        if info_teacher == 1:  # информация о студентах (для преподавателей)
            info_1 = int(
                input('1 - информация об одном студенте, 2 - информация о группе:\n'))
            if info_1 == 1:  # инфо об одном студенте (для преподавателей)
                info_one = input('Введите ФИО студента:\n')
                for i in range(len(students)):
                    if students[i]['ФИО'] == info_one:
                        print(f'{students[i]["ФИО"]}: {students[i]["статус"]}, {students[i]["телефон"]}, '
                              f'{students[i]["факультет"]}, {students[i]["группа"]}.')
                        return 0
                print(f'Студент с таким именем не найден.')
                users_request(students, teachers, status)
            elif info_1 == 2:  # состав группы студентов (для преподавателей)
                info_group = input('Введите номер группы:\n')
                group_list = []
                count = 0
                for i in range(len(students)):
                    if students[i]['группа'] == info_group:
                        group_list.append(students[i]['ФИО'])
                        count += 1
                if count != 0:
                    print(
                        f'В группе {info_group} состоят следующие студенты:')
                    for fio in group_list:
                        print(fio)
                    return 0
                else:
                    print('Группа с таким именем не найдена.')
                    users_request(students, teachers, status)
        # информация о преподавателях (для преподавателей)
        elif info_teacher == 2:
            info_teach = input('Введите ФИО преподавателя:\n')
            for i in range(len(teachers)):
                if teachers[i]['ФИО'] == info_teach:
                    print(f'{teachers[i]["ФИО"]}: {teachers[i]["статус"]}, {teachers[i]["институт"]}, '
                          f'{teachers[i]["кафедра"]}.')
                    return 0
            print('Преподаватель с таким именем не найден.')
            users_request(students, teachers, status)
        else:
            print('Неверный запрос.')
    else:
        info_students = int(input(
            'Какая информация Вас интересует: 1 - данные преподавателя, 2 - данные студентов'))
        if info_students == 1:  # информация о преподавателях (для студентов)
            info_te = input('Введите ФИО преподавателя:\n')
            for i in range(len(teachers)):
                if teachers[i]['ФИО'] == info_te:
                    print(
                        f'{teachers[i]["ФИО"]}: {teachers[i]["почта"]}, {teachers[i]["институт"]}.')
                    return 0
            print('Преподаватель с таким именем не найден.')
            users_request(students, teachers, status)
        elif info_students == 2:  # информация о студентах (для студентов)
            info_one = input('Введите ФИО студента:\n')
            for i in range(len(students)):
                if students[i]['ФИО'] == info_one:
                    print(
                        f'{students[i]["ФИО"]}: {students[i]["почта"]}, {students[i]["факультет"]}.')
                    return 0
            print(f'Студент с таким именем не найден.')
            users_request(students, teachers, status)
        else:
            print('Неверный запрос.')
