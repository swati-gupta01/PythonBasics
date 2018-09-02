#decorators widely use the concept of closure

def firstClass(film):
    '''nonlocal arguments can be read by the inherited function'''
    #inherited class
    def inherited():
        '''nonlocal arguments can be read by the inherited function
        id of inherited= a'''
        print('film name is :',film)
    print(id(inherited))
    return inherited

a = firstClass('Thor') #a=inherited
print('a:',a)
print(id(a))
#calling inherited()
a()
#All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function.
print(a.__closure__)
# The cell object has the attribute cell_contents which stores the closed value.
print(a.__closure__[0].cell_contents)
