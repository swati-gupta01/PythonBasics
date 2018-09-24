
def print_fun(arg):
    def printer():
        # nonlocal arg
        # arg=arg+2
        print(arg)
        print(id(printer))
    return printer
a=print_fun(2) #a=printer
b=print_fun(2)
# a()  #printer()
# del print_fun
print(a.__closure__)
print(b.__closure__)
print(a.__closure__[0].cell_contents)
print(b.__closure__[0].cell_contents)

