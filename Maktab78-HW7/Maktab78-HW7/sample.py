from person import Person
import logging

logging.basicConfig(level=logging.INFO, filename='sample.log',
                    format="%(asctime)s — %(name)s — %(message)s")

logger_sample = logging.getLogger()


def sub(a, b):
    if b != 0:
        return a / b
        logger_sample.debug("a/b=" + str(a / b))

    logger_sample.error("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)

# class test:
#     def __init__(self, a) -> None:
#         self.a = a

#     @property
#     def a(self):
#         return self._a

#     @a.setter
#     def a(self, val):
#         if val > 10:
#             self._a = val
#             print(val)
#         else:
#             self._a = 0
#             print(val+3)


# t = test(1)
# print(t._a)
# print(t.a)

# logging.basicConfig(level=logging.INFO)
# logging.info("Hey")
