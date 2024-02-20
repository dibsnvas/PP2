def squares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2


print(*squares(10, 20))
