def type_logger(func):
    def tag_wrapper(arg):
        return f'{arg}: {type(arg)}'
    return tag_wrapper


@type_logger
def calc_cube(x):
   return x ** 3

print(calc_cube(5))