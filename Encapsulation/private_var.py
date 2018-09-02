'''
Using OOP in python , we can restrict access to methods
and variables.This prevent data from direct modification ,
called as ENCAPSULATION.
'''

class Compute:
    """Understanding Private Variables '_' or '__'"""
    def __init__(self,maxprice):
        self.__maxprice=maxprice

    # #getter -If this is not defined __var will act as normal var
    def get_maxprice(self):
        print('id under getter: ',id(self.__maxprice))
        print('Price:',self.__maxprice)

    #setter
    def set_maxprice(self,value):
        self.__maxprice=value


c=Compute(500)
c.get_maxprice()
# actual value will not get updated and it will read it as different varaible
c.__maxprice =1200
print('id outside: ',id(c.__maxprice))
print(c.__maxprice)
c.get_maxprice()
#calling setter to update value
c.set_maxprice(2000)
c.get_maxprice()

#docstring and help
# print(Compute.__doc__)
# help(Compute)


