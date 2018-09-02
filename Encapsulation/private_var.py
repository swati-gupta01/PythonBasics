'''
Using OOP in python , we can restrict access to methods
and variables.This prevent data from direct modification ,
called as ENCAPSULATION.
'''

class Compute:
    """Understanding Private Variables '_' or '__'"""
    def __init__(self):
        self.__maxprice=900

    #getter -If this is not defined __var will act as normal var
    def get_maxprice(self):
        print('Price:',self.__maxprice)

    #setter
    def set_maxprice(self,value):
        self.__maxprice=value


c=Compute()
c.get_maxprice()
#value will not get updated
c.__maxprice =100
c.get_maxprice()
#calling setter to update value
c.set_maxprice(1000)
c.get_maxprice()

#docstring and help
print(Compute.__doc__)
help(Compute)


