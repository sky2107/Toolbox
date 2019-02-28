# Problems in python

> mutable default argument 

    def f(x=[]):
        x.append(len(x))
        return x

    print(f'f() is {f()}')
    print(f'f() is {f()}')
    print(f'f() is {f()}')

    =>  f() is [0]
        f() is [0, 1]
        f() is [0, 1, 2]

> solving it

    def f(*args, **kwargs):
        def f(x=[]):
            x.append(len(x))
            return x
    return f(*args, **kwargs)
