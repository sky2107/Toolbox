# UTUBE

> question from itertools import islice, tee <br>
> zip modul

> Examples of the above modules

> zip code example

    first = [x for x in range(11)]
    second = [x for x in reversed(first)]

    combine = zip(first, second)

    for c in combine:
        print(c)
        
    (0, 10)
    (1, 9)
    (2, 8)
    (3, 7)
    (4, 6)
    (5, 5)
    (6, 4)
    (7, 3)
    (8, 2)
    (9, 1)
    (10, 0)

[Generators pyData](https://www.youtube.com/watch?v=XEn_99daJro&t=11s)

1. first.py 0 - 11 minutes into the video
2. second.py 11 - 20 minutes

> plus function advanced stuff code examples

> Global example

    z = 0
    def add(x, y):
        'add function'
        global z
        z += 1
        return x + y + z

> another way to call a parameter in a func

    def add(x, y):
        'add function'
        add.z += 1
        return x + y + add.z

    if __name__ == '__main__':
        add.z = 0
        print((add(1,2)))
        print((add(2,1)))

> more complicated

    def add(z=0):
        def add(x, y):
            'add function'
            nonlocal z
            z += 1
            return x + y + z
    return add

    add_l = lambda x, y: x + y

    if __name__ == '__main__':
        add_1 = add()
        add_2 = add()
        print((add_1(1,2)))
        print((add_2(2,1)))
        print((add_1(2,1)))

> creating an generator

    from time import sleep
    from random import randrange

    def compute():
        sleep(.1)
        return randrange(10)

    # print(compute())

    def f():
        rv = []
        for i in range(10):
            rv.append(compute())
        return rv

    print(f()) 
    print(f'f:{f()}') # will print out whole list both lines of code
    => f:[8, 0, 0, 7, 9, 9, 2, 3, 5, 9] # e.g.