first = [x for x in range(11)]
second = [x for x in reversed(first)]

combine = zip(first, second)

for c in combine:
    print(c)