def decorator_f(fun):
    def wrapper_f(*args,**kvargs):
        print('yeh decorated before',fun.__name__)
        fun(*args,**kvargs)
    return wrapper_f

@decorator_f   #same as display=(decorator_f(display)) 
def display():
    print('Function display run')
@decorator_f
def display_info(name,age):
    print('Name is {} and age is {}'.format(name,age))


# display=(decorator_f(display))  #executing wrapper which is executing name func
display()
display_info('Swati',25)


