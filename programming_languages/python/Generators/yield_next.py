def countdown(n):
    print('Starting count from ', n)
    while n > 0:
        yield n
        n -= 1
    print('done')

c = countdown(3)

print(c)

print(next(c))
print(next(c))
print(next(c))
print(next(c))