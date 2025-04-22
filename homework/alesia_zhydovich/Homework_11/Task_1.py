class Book:
    page_material = 'paper'
    text_available = True


    def __init__(self, title, author, page_numbers, isbn, reserved):
        self.title = title
        self.author = author
        self.page_numbers = page_numbers
        self.isbn = isbn
        self.reserved = reserved


    def print_info(self):
        base_info = (
            f'Название: {self.title}, '
            f'Автор: {self.author}, '
            f'страниц: {self.page_numbers}, '
            f'материал: {self.page_material}'
        )
        print(base_info + ', зарезервирована' if self.reserved else base_info)


books = [
    Book('Math for child', 'Assa S', 34, 'ISBN0023456', False),
    Book('Harodnia', 'Sapega', 500, 'ISBN123456', False),
    Book('1984', 'Orwell', 328, 'ISBN654321', False),
    Book('Zamok', 'Karatkevich', 1225, 'ISBN789456', False),
    Book('Idiot', 'Dostoevsky', 500, 'ISBN123456', True)
]

for book in books:
    book.print_info()


class WorkBook(Book):
    def __init__(self, title, author, page_numbers, isbn, reserved, subject, level):
        super().__init__(title, author, page_numbers, isbn, reserved)
        self.subject = subject
        self.level = level


    def print_info(self):
        base_info = (
            f'Название: {self.title}, '
            f'Автор: {self.author}, '
            f'страниц: {self.page_numbers}, '
            f'предмет: {self.subject}, '
            f'класс: {self.level}'
        )
        print(base_info + ', зарезервирована' if self.reserved else base_info)


workbooks = [
    WorkBook('Алгебра', 'Жук', 200, 'ISBN001', False, 'Математика', 9),
    WorkBook('История', 'Гусь', 180, 'ISBN002', False, 'История', 8),
    WorkBook('География', 'Судак', 150, 'ISBN003', True, 'География', 7)
]

for wb in workbooks:
    wb.print_info()
