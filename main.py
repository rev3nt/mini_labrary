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
            library_dict[title] = {'author': author, 'year': year, 'availability': None}

            print(f'\nРедактирование книги \"{title}\" прошло успешно!\n')
    else:
        library_dict[title] = {'author': author, 'year': year, 'availability': None}

        print(f'\nКнига \"{title}\" успешно добавлена в библиотеку\n')


def delete_book(title, library_dict):
    if title in library_dict:
        del library_dict[title]

        print(f'\nКнига \"{title}\" была успешно удалена\n')
    else:
        print(f'\nКниги \"{title}\" нет в библиотеке\n')


library = {
    'Гарри Поттер и узник Азкабана': {'author': 'Джоан Роулинг', 'publication_year': 2021, 'available': True},
    'Зеленая миля': {'author': 'Стивен Кинг', 'publication_year': 2025, 'available': False}
}

book_list_view(library)

add_book('Ванпис', 'Эйитиро Ода', 1980, library)

book_list_view(library)

add_book('Ванпис', 'Хидео Кадзима', 1984, library)

book_list_view(library)

delete_book('Ванпис', library)

book_list_view(library)