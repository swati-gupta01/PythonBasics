class Employee:

    def __init__(self, first):
        self._first = first

    @property
    def first(self):
        print('getter')
        return self._first

    @first.setter
    def first(self, value):
        print('setter')
        self._first = value

    @first.deleter
    def first(self):
        print('deleter')
        del self._first
    
    #sec=property(getFirst,setFirst,delFirst,"first")
    
emp = Employee('Swati')

print(emp.first)

emp.first = 'Abhinav'

print(emp.first)

del emp.first