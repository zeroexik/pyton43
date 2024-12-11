class Book:
    def __init__(self, name, autor, year, page, price):
        self.name = name
        self.autor = autor
        self.year = year 
        self.page = page 
        self.price = price
        
    def calculate_cost(self):
        return (self.price * self.page) / 200
    
    def change_page(self, new_page):
        self.page = new_page

my_book = Book("Ромео и Джульетта", "Уильям Шекспир",  1596, 192, 500)

print(f"название: {my_book.name}")
print(f"автор: {my_book.autor}")
print(f"год: {my_book.year}")
print(f"страницы: {my_book.page}")
print(f"цена: {my_book.price}")

cost = my_book.calculate_cost()
print(f"стоимость книги: {cost} руб.")
my_book.change_page(200)
print(f"обновлённое количество страниц: {my_book.page}")