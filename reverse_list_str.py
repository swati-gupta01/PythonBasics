#reverse a list

l= [1,2,3]
#Method 1
print(list(reversed(l)))
#Method 2
print(l[::-1])
#Method 3
t=[]
for i in l[::-1]:
    t.append(i)
print(t)
#Method 4
print([i for i in l[::-1]])
#method 5
def rev(l):
    le=len(l)
    for i in range(int(le/2)):
        j=le-i-1
        l[i],l[j]=l[j],l[i]
    print(l)
rev([1,2,3,4,5,6,7,8,9,10,11])

#reverse a integer
def rev(i):
    temp = 0
    while i != 0:
        a = (i % 10)  # 2
        i = int(i / 10)  # 1
        temp = (10 * temp) + a

    print(temp)


rev(123)










