# Dream_team
Task for team work

1. Чтобы развернуть проект необходимо склонировать репозиторий
2. Чтобы запустить проект необходимо запустить скрипт main.py
3. Пройдите авторизацию, если вы новый пользователь, то вам будет предложена регистрация. После авторизации вам предлагается выбрать то, что вас интересует. В зависимости от вашего статуса: учитель или ученик, вам будет предложен различные варианты того, с какой информацией о других пользователях вы можете ознакомиться. Удобной функцией для учителя является вывод списка группы, а для ученика вывод почты учителя.


05.09
Anna (team lead): https://github.com/Koannko
Pavel: https://github.com/seroglazkinpavel/Python
Lev: https://github.com/DarLeoo
Elena: https://github.com/Tigreshkas

Задача:
Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.

Модули:
1. Контроллер. Общение с пользователем, логика (Анна)
2. Модель. Чтение данных из файла (Лев)
3. Вью. Показать данные пользователю, интерфейс (Павел)

Модель. Структура текстового файла:
1. Фамилия Имя Отчество
2. Статус
3. Номер телефона родителей (у ученика), эл. почта (у учителя)
4. Институт
5. Группа (у ученика), кафедра (у учителя)
6. Разделитель - пустая строка

Предложения для развития. Реализовать функционал:
1. Запросить данные у пользования (регистрация нового ученика / учителя)
2. Сохранение данных нового пользователя в файл


06.09
Схема работы: https://miro.com/app/board/o9J_lSHYkgI=/?share_link_id=302233537409

07.09 
Встречаемся также, в 19:20 (мск). Stand up

08.09
Необходимо реализовать функции:
Павел:
  * Получение ФИО в файл
  * Вывод надписи "зарегистрируйтесь"
  * Вывод надписи "введен неверный пароль"
  * Вывести список вариантов. Для учителя и для ученика предлагаются разные.*

Лев, Елена:
  * Сравнить ФИО с ключами в словарях ученики и учителя
  * Сравнить пароль данного ключа с введенным паролем
  * Получение статуса, телефона и т.д. по ФИО. На вход ФИО и название интересующего ключа
  * Сформировать словарь. На вход подается "ученики" или "учителя"
  * Сформировать список группы. Выводит ФИО учеников
  * Получить расписание группы