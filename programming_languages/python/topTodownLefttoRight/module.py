# module.py

# global variable
a = 10

def get_a():
    global _a
    return a

def set_a(value):
    global _a
    if value < 0:
        raise Exception('must be positive')
    _a = value

class A:
    def __init__(self, b):
        self._b = b

    @property
    def b(self, value):
        return self._b

    @b.setter
    def b(self, value):
        if value < 0:
            raise Exception('must be positive')
        self._b = value

class B:
    pass