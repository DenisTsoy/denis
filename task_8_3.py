def type_logger(*args, **kwargs):
    def loger(*args, **kwargs):
        for _ in args:
            print(f'{_}: {type(_)}')
    return loger


@type_logger
def calc_cube(*args, **kwargs):
    return x**3


a = calc_cube(5,3,6,7)
print(a)
