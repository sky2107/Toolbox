from time import sleep
from random import randrange

def compute():
    sleep(.1)
    return randrange(10)

# print(compute())

def f():
    rv = []
    for _ in range(10):
        rv.append(compute())
    return rv

print(f())
print(f'f:{f()}')