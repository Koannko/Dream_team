def new_user(dates):
    """Функция записи нового пользователя в файл"""
    if 'учитель' in dates:
        with open("Teachers.txt", "a", encoding="utf-8") as f:
            f.writelines(f'\n{dates}')
    else:
        with open("Students.txt", "a", encoding="utf-8") as f:
            f.writelines(f'\n{dates}')
