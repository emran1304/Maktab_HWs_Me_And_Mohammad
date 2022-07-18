class Person:
    
    def __init__(self, name, e_mail = None, gender = None):
        self.name = name
        self.e_mail = e_mail 
        self.gender = gender

class Author(Person):
    
    def __init__(self, name, e_mail, gender, author_code, genre = None):
        super().__init__(name, e_mail, gender)
        self.author_code = author_code
        self.genre = genre
        
class Poet(Person):
    
    
    def __init__(self, name, e_mail, gender, genre = None):
        super().__init__(name, e_mail, gender)
        self.genre = genre
        
class Research(Person):
    
    def __init__(self, name, e_mail, gender, major, university = None):
        super().__init__(name, e_mail, gender)
        self.major = major
        self.university = university
        