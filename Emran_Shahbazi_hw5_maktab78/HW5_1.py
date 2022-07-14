class Singelton:
    instance = None

    @staticmethod
    def get_instance():
        if Singelton.instance is None:
            Singelton.instance = Singelton()
        return Singelton.instance


s1 = Singelton.get_instance()
s2 = Singelton.get_instance()
s3 = Singelton()
s4 = Singelton()
print(s1 == s2)
print(s3 == s4)
