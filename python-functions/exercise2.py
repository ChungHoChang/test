def print_args(*args):
    # for arg in args:
    #     print(f'arg = {arg}')
    print(args)
    print(type(args))


print_args('a')
print_args('a', 'b')
print_args('a', 'b', 'c')
