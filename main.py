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


def issue_book(title,library_dict):
    if title in library_dict:
        if library_dict[title]['available'] is False:
            print(f'\nКнига \"{title}\" уже выдана\n')
        else:
            library_dict[title]['available'] = False

            print(f'\nКнига \"{title}\" была успешно выдана\n')
    else:
        print(f'\nКниги \"{title}\" нет в базе библиотеки\n')


def return_book(title,library_dict):
    if title in library_dict:
        if library_dict[title]['available'] is True:
            print(f'\nКнига \"{title}\" уже в библиотеке\n')
        else:
            library_dict[title]['available'] = True

            print(f'\nКнига \"{title}\" успешно вернулась в библиотеку\n')
    else:
        print(f'\nКниги \"{title}\" нет в базе библиотеки\n')


def find_book(title,library_dict):
    if title in library_dict:
        print(f'\"{title}\".\nАвтор: \"{library_dict[title]["author"]}\"')

        print(f'Дата публикации: {library_dict[title]["publication_year"]}')

        if library_dict[title]["available"] is None:
            print('Книга в библиотеке, но ее статус не определен')
        else:
            print(f'{"Книга доступна\n" if library_dict[title]["available"] == True else "Книга выдана\n"}')
    else:
        print(f'Книги \"{title}\" нет в базе данных\n')


library = {
    'Гарри Поттер и узник Азкабана': {'author': 'Джоан Роулинг', 'publication_year': 2021, 'available': True},
    'Зеленая миля': {'author': 'Стивен Кинг', 'publication_year': 2025, 'available': False}
}

book_list_view(library)

add_book('Преступление и наказание', 'Ф. М. Достоевский', 1866, library)

add_book('Зеленая миля', 'Стивен Кинг', 2021, library)

delete_book('Гарри Поттер и узник Азкабана', library)

find_book('Преступление и наказание', library)

issue_book('Преступление и наказание', library)

return_book('Зеленая миля', library)

issue_book('Преступление и наказание', library)

book_list_view(library)