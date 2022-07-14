class Student:

    def __init__(self, fname, lname, age, number, email, **kw):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.number = number
        self.email = email

        for i in kw.keys():
            self.__setattr__(i, kw[i])

        self.x = {'first_name': self.fname, 'last_name': self.lname, 'age': self.age, 'email': self.email}

        for k, v in kw.items():
            self.x[k] = v

    def data(self):
        return self.x


reza = Student('Reza', 'Amiri', 22, 9121111111, 'mail@gmail.com' , lang= 'fa-IR')
print(reza.data())
print(type(reza.data()))


