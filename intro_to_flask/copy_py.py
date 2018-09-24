a=[1,2,3,[1,2,4]]
b=a.copy()
a=[1,2,3,[1,4]]
print(id(a))
print(id(b))
print(b)