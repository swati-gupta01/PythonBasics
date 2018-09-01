class Employee:

    def __init__(self, first):
        self.first = first

    @property
    def getFirst(self):
        print('getter')
        return self.first

    @getFirst.setter
    def getFirst(self, value):
        print('setter')
        self.first = value

    @getFirst.deleter
    def getFirst(self):
        print('deleter')
        del self.first
    
    #sec=property(getFirst,setFirst,delFirst,"first")
    
emp = Employee('Swati')

print(emp.getFirst)

emp.getFirst = 'Abhinav'

print(emp.getFirst)

del emp.getFirst