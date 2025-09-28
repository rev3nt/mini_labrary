def book_list_view(library_dict):
    if len(library_dict) != 0:
        for book in library_dict:
            print(book)
        return None

    print('Библиотека пуста')


library = {
    'Гарри Поттер и узник Азкабана': {'author': 'Джоан Роулинг', 'publication_year': 2021, 'available': True},
    'Зеленая миля': {'author': 'Стивен Кинг', 'publication_year': 2025, 'available': False}
}

book_list_view(library)
