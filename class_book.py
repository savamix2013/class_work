"""Клас книги в бібліотеці"""

class Book:
    """Описуємо книгу"""

    def __init__(self, title, author, year, pages, genre):
        """інціалізувати атрибути, що описують книжку"""
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.genre = genre
        

    def get_descriptive_name(self):
        """Повернути відформатоване ім"я"""
        long_name = f"{self.title} {self.author} {self.year} {self.pages}"
        return long_name.title()
    
    def get_info(self):
        """Повертає інформацію про книгу у вигляді рядка"""
        return f"Назва: {self.title}, Автор: {self.author}, Рік видання: {self.year}, Сторінок: {self.pages}"

    def is_modern(self):
        """Перевіряє, чи книга сучасна (видана після 2010 року)."""
        return self.year > 2010
    
    def is_genre(self, ):
        
    

book1 = Book("Гаррі Поттер", "Дж. К. Ролінг", 2007, 500, "Фентезі")
book2 = Book("Python для початківців", "Джон До", 2015, 350, "Література")

print(book1.get_info(), book1.is_modern())  # Виведе інформацію про книгу
print(book2.get_info(), book2.is_modern())  # Виведе: Назва: Python для початківців, Автор: Джон До, Рік видання: 2015, Сторінок: 350
# print(book1.is_modern())
# print(book2.is_modern())