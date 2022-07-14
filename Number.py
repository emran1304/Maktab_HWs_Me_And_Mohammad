class Number:
    def __init__(self, v):
        self.v = v
        # if isinstance(v, int):
        #     self.__class__ = int
        # if isinstance(v, float):
        #     self.__class__ = float

    def __add__(self, other):
        return self.v + other.v

    def __sub__(self, other):
        return self.v - other.v

    def __mul__(self, other):
        return self.v * other.v

    def __truediv__(self, other):
        return self.v / other.v

    def __gt__(self, other):
        return self.v > other.v

    def __lt__(self, other):
        return self.v < other.v

    def __eq__(self, other):
        return self.v == other.v


n = Number(5.2)
print(type(n))