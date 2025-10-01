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
    if library_dict[title]['available']:
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
7: Выйти из программы'''

while True:
    print(options)

    user_input = input('Введите номер опции: ')

    if user_input == '1':
        book_list_view(library)
    elif user_input == '2':
        try:
            input_title = input('Введите название добавляемой/редактируемой книги: ')

            input_author = input('Введите автора книги: ')

            input_year = int(input('Введите год публикации: '))

            add_book(input_title, input_author, input_year, library)
        except ValueError:
            print('Год введен некорректно')
    elif user_input == '3':
        input_title = input('Введите название книги, которую хотите удалить: ')

        delete_book(input_title, library)
    elif user_input == '4':
        input_title = input('Введите название книги для выдачи: ')

        issue_book(input_title, library)

    elif user_input == '5':
        input_title = input('Введите название книги для возврата: ')

        return_book(input_title, library)
    elif user_input == '6':
        input_title = input('Введите название книги для поиска: ')

        find_book(input_title, library)
    elif user_input == '7':
        break
    else:
        print('Введите опцию из меню!\n')