'''
Using OOP in python , we can restrict access to methods
and variables.This prevent data from direct modification ,
called as ENCAPSULATION.
'''

class Compute:
    """Understanding Private Variables '_' or '__
    _ act as normal var
    __ variable can't be read or modified directly'"""
    def __init__(self,maxprice):
        self.__maxprice=maxprice

    def get_maxprice(self):
        print('id under getter: ',id(self.__maxprice))
        print('Price:',self.__maxprice)

c=Compute(500)
try:
    print(c.__maxprice)  #through error
except:
    c.get_maxprice()

