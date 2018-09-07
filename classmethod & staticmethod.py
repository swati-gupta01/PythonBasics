class Pizza:
    def __init__(self,top):
        self.top=top

    def __repr__(self):
        return ('Pizza{'+str(self.top)+'}')

    @classmethod
    def marg(cls):
        return cls(['cheese','tomato'])

    @staticmethod #class level method-1 copy
    def sta():
        return 'I am static'

a=Pizza(['cheeze','onion'])
b=Pizza.marg()
print(a)
print((b))
print(Pizza.sta())
print(b.sta())

