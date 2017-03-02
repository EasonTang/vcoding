import datetime


def hello():
    print('Hello', datetime.datetime.now())


class Person:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    p = Person('Eason')
    print(p.name)