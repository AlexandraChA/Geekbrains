def val_checker(condition):
    def wrap(func):
        def wrapper(arg):
            con = (condition)(arg)
            if con:
                markup = func(arg)
                return markup
            else:
                 msg = f'wrong val {arg}'
                 raise ValueError(msg)
        return wrapper
    return wrap


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

print(calc_cube(5))


