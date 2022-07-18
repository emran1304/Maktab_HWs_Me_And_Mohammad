import logging

logging.basicConfig(level=logging.DEBUG, filename='person.log',
                    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s")
logger_person = logging.getLogger()


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logger_person.warning("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logger_person.critical("Invalid age!")
        self._age = 0
