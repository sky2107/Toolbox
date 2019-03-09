# __title__ = 'Generators'
# __author__ = 'James Powell'
# __email__ = 'email@adress'
# __twitter__ = 'twitter_account'


# from builtins import print as _print

# def print(*args,first=[True], **kwargs):
#     _print(*args, **kwargs)
#     if first and first.pop():
#         _print(f'Follow me on twitter @(__twitter__)'.rjust(80, ' '))

# if __name__ == '__main__':
#     print(__title__)
#     print(__author__)
#     print(__email__)
#     print(__twitter__)
# z = 0
def add(z=0):
    def add(x, y):
        'add function'
        # global z
        nonlocal z
        z += 1
        return x + y + z
    return add

add_l = lambda x, y: x + y

if __name__ == '__main__':
    print(type(add_l))
    print(type(add))
    # add.z = 0
    add_1 = add()
    add_2 = add()
    print((add_1(1,2)))
    print((add_2(2,1)))
    print((add_1(2,1)))
    # monkey back doc 
    add_l.__doc__ = 'add lambdi funci'
    add_l.__name__ = 'add_lam'
    help(add)
    help(add_l)
    