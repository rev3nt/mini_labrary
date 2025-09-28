def book_list_view(library_dict):
    if len(library_dict) != 0:
        for book in library_dict:
            print(book)
    else:
        print('Библиотека пуста')


def add_book(title, author, year):
    if title in library:
        print("Данная книга уже добавлена в библиотеку, хотите изменить информацию о ней(Y/N)? ")

        user_answer = input().lower()

        if user_answer == 'y':
            library[title] = {'author': author, 'year': year, 'availability': None}

            print(f'Редактирование книги \"{title}\" прошло успешно!')
    else:
        library[title] = {'author': author, 'year': year, 'availability': None}

        print(f'Книга \"{title}\" успешно добавлена в библиотеку')


library = {
    'Гарри Поттер и узник Азкабана': {'author': 'Джоан Роулинг', 'publication_year': 2021, 'available': True},
    'Зеленая миля': {'author': 'Стивен Кинг', 'publication_year': 2025, 'available': False}
}

book_list_view(library)

add_book('Ванпис', 'Эйитиро Ода', 1980)

book_list_view(library)

add_book('Ванпис', 'Хидео Кадзима', 1984)

book_list_view(library)
