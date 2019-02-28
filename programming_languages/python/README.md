# Python

# Question

1. How does it work???? sum(arr_new_2, 1))
2. buildin methods for list

> linux enviroment

    sudo apt-get install python3-venv
    # creating enviroment
    python3 -m venv folder_name
    cd folder_name
    . bin/activate

> sources books and utube

#
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

# Generators 

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

> Getter and Setter in a Class

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