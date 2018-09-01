#we can modify the variables , by just calling variables as attributes , not as functions
#property will automatically call getter , setter and deleter methods

class Employee:

    def __init__(self, first):
        self._first = first
     #getter
    def getFirst(self):
        print('getter')
        return self._first

    #setter
    def setFirst(self, value):
        print('setter')
        self._first = value

    #deleter
    def delFirst(self):
        print('deleter')
        del self._first

    #initialize property
    first=property(getFirst,setFirst,delFirst,"Property Decorator type 1")


emp = Employee('Swati')

print(emp.first)

emp.first = 'Abhinav'

print(emp.first)

del emp.first