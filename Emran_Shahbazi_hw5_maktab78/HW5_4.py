# class Add:
#
#     def __init__(self, v):
#         self.v = v
#
#     def __call__(self, a = 0):
#         x = self.v + a
#         w = Add(x)
#
#         return w
#
#     def __str__(self):
#         return str(self.v)
#
# print(Add(5)(10)(20))

from abc import ABC, abstractmethod, abstractproperty
from uuid import uuid4


class DollarMixin:

    def ind_property(self):
        self.name = 'dollar'
        self.symbol = '$'


class EuroMixin:

    def ind_property(self):
        self.name = 'euro'
        self.symbol = 'E'


class RialMixin:

    def ind_property(self):
        self.name = 'rial'
        self.symbol = 'R'


class Money(ABC):

    @abstractmethod
    def __int__(self, val):
        self.val = val

    @abstractproperty
    def rate():
        pass


class Dollar(Money, DollarMixin):
    rate = 1

    def __int__(self, value):
        super().__init__(value)
        self.ind_property()


class Credit:

    def __init__(self, **kw):
        for k, v in kw.items():
            # setattr(self, k, v
            self.__setattr__(k, v)

        # self.__dict__.update()


class Receipt:

    def __init__(self, **kw):
        self.__dict__.update()


class Wallet:

    __id = None

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.__id = str(uuid4()).split('-')[0]
            cls.pocket = {}
            cls.receipt = {}
            cls.credit = {}
            print(f"Code is: {cls.__id} ")
            cls.__recovery = cls.__set_recovery()
        else:
            return cls.instance

    @classmethod
    def __set_recovery(cls):
        question = input("Enter a question:")
        answer = input("Enter your answer to this question!")

        return {question: answer}

    def __log(cls, value):




























