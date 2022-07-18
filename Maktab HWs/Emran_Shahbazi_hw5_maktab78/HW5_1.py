'''
Method No.1
'''

class Singelton:
    instance = None

    @staticmethod
    def get_instance():

        if Singelton.instance == None:
            Singelton.instance = Singelton()
        return Singelton.instance


s1 = Singelton.get_instance()
s2 = Singelton.get_instance()
print(s1 == s2)

'''
Method No.2
'''

class Singleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()

print(s1 == s2)