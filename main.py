def book_list_view(library_dict):
    if len(library_dict) != 0:
        for book in library_dict:
            print(book, library_dict[book])
    else:
        print('\nБиблиотека пуста\n')


def add_book(title, author, year, library_dict):
    if title in library_dict:
        print("Данная книга уже добавлена в библиотеку, хотите изменить информацию о ней(Y/N)? ")

        user_answer = input().lower()

        if user_answer == 'y':
            library_dict[title] = {'author': author, 'publication_year': year, 'available': None}

            print(f'\nРедактирование книги \"{title}\" прошло успешно!\n')
    else:
        library_dict[title] = {'author': author, 'publication_year': year, 'available': None}

        print(f'\nКнига \"{title}\" успешно добавлена в библиотеку\n')


def delete_book(title, library_dict):
    if title in library_dict:
        del library_dict[title]

        print(f'\nКнига \"{title}\" была успешно удалена\n')
    else:
        print(f'\nКниги \"{title}\" нет в библиотеке\n')


def issue_book(title, library_dict):
    if title not in library_dict:
        print(f'\nКниги \"{title}\" нет в базе библиотеки\n')

        return
    if not library_dict[title]['available']:
        library_dict[title]['available'] = False

        print(f'\nКнига \"{title}\" была успешно выдана\n')
    else:
        print(f'\nКнига \"{title}\" уже выдана\n')


def return_book(title, library_dict):
    if title not in library_dict:
        print(f'\nКниги \"{title}\" нет в базе библиотеки\n')

        return
    if library_dict[title]['available']:
        print(f'\nКнига \"{title}\" уже в библиотеке\n')
    else:
        library_dict[title]['available'] = True

        print(f'\nКнига \"{title}\" успешно вернулась в библиотеку\n')


def find_book(title, library_dict):
    if title not in library_dict:
        print(f'Книги \"{title}\" нет в базе данных\n')

        return

    print(f'\"{title}\"\nАвтор: \"{library_dict[title]["author"]}\"')

    print(f'Дата публикации: {library_dict[title]["publication_year"]}')
    if library_dict[title]['available'] is None:
        print('Книга в библиотеке, но ее статус не определен')

        return
    else:
        print(f'{"Книга доступна\n" if library_dict[title]["available"] else "Книга выдана\n"}')

        return


library = {
    'Гарри Поттер и узник Азкабана': {'author': 'Джоан Роулинг', 'publication_year': 2021, 'available': True},
    'Зеленая миля': {'author': 'Стивен Кинг', 'publication_year': 2025, 'available': False}
}

options = '''\n1: Просмотреть полный список книг
2: Добавить/Редактировать книгу
3: Удалить книгу
4: Выдать книгу
5: Вернуть книгу 
6: Найти книгу 
7: Выйти из программы\n'''

func_dict = {
    '1': lambda: book_list_view(library),
    '2': lambda: add_book(input('Введите название добавляемой/редактируемой книги: '),
                          input('Введите автора книги: '), int(input('Введите год публикации: ')),library),
    '3': lambda: delete_book(input('Введите название удаляемой книги: '), library),
    '4': lambda: issue_book(input('Введите название книги для возврата: '), library),
    '5': lambda: return_book(input('Введите название книги для выдачи: '), library),
    '6': lambda: find_book(input('Введите название книги для поиска: '), library),
}

while True:
    print(options)

    user_input = input('Введите номер опции: ')

    if user_input == '7':
        break

    if user_input in func_dict:
        try:
            func_dict[user_input]()
        except ValueError:
            print('Год введен некорректно!')
    else:
        print('Введите опцию из меню!\n')