# import uuid
#
#
# class Human:
#     __COUNTER: int = 0
#
#     # HUMANS = []
#
#     def __init__(self, name: str, age: int):
#         # self.__class__.HUMANS.append(self)
#         self.__class__.__COUNTER += 1
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def get_counter(cls):
#         return cls.__COUNTER
#
#
# class Category:
#     _category = []
#
#     def __init__(self, cat_name, shelf=[]):
#         self.cat_name = cat_name
#         self.shelf = shelf
#         self.cat_id = str(uuid.uuid4()).split('-')[0]
#         self.__class__._category.append(cat_name)
#
#     @property
#     def cat_name(self, ):
#         return self._cat_name
#
#     @cat_name.setter
#     def cat_name(self, name):
#         if name in self.__class__._category:
#             raise f"This category already exists"
#         else:
#             self._cat_name = name
#
#
# class Shelf:
#     _shelf = []
#
#     def __init__(self, category: Category):
#         self.__class__._shelf.append(self)
#         self.category = category
#         self.shelf_id = str(len(self.__class__._shelf)) + "-" + category.cat_id
#         self.pages = 0
#         self.books = []
#
#     def add_book(self, book):
#         if self.pages + book.n_page <= 10000 and self.category == book.category:
#             self.books.append(book)
#             self.pages += book.n_page
#
#         else:
#             raise f"Add another book is not possible"
#
#
# class Author(Human):
#     def __init__(self, name, age, author_id):
#         super.__init__(name)
#         self.author_id = author_id
#
#
# class Book:
#     def __init__(self, title, n_page, author: Author, price, category: Category):
#         self.title = title
#         self.n_page = n_page
#         self.author = author
#         self.price = price
#         self.category = category
#
#
# class Container:
#     def __init__(self, name, shelves: list):
#         self.name = name
#         self.shelves = shelves
#
#     def add_shelf(self, shelf):
#         self.shelves.append(shelf)
#
#     def __len__(self):
#         count = 0
#         for i in self.shelves:
#             count += len(i.books)
#
#         return count
#
#
# class Library:
#
#     # aggregation
#     def __init__(self, name, staff, containers: list) -> None:
#         self.name = name
#         self.staff = staff
#         self.containers = containers
#
#
# class Staff(Human):
#
#     def __init__(self, name: str, age: int, staff_id: int, library: Library):
#         super().__init__(name, age)
#         self.staff_id = staff_id
#         self.library = library
#
#     def search(self, *, name=None, id=None, author_name=None, author_code=None):
#         search_lst = []
#
#         if name is not None:
#             for i in self.library.containers:
#                 for j in i.shelves:
#                     for k in j.books:
#                         if name == k.title:
#                             search_lst.append(k)
#
#         elif
#
#     def get(self):
#
#     def give_back(self):

lst = list(range(7))
l = list(range(7, 14))
print(list(map(lambda x, y: x*y, lst, l)))
print(l)
