from person import Person
import logging

logging.basicConfig(level=logging.WARNING, filename='sample.log',format="%(asctime)s — %(name)s — %(levelname)s — %(message)s")


def sub(a, b):

    if b != 0:
        return a / b
        logging.debug("a/b=" + str(a / b))

    logging.error("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)