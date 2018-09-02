'''assert statement is used as debugging tool as it halts the program at the point where an error occurs.
assert statement has a condition and if the condition is not satisfied the program will stop and give AssertionError
'''

def divide(a,b):
    '''divide function will take 2 values and divide
    need to check if b !=0'''

    #asset needs to be true , takes condition and error statement
    assert b != 0, 'B is zero'
    return a/b

#as input always take a string , converting to float
a=float(input('Enter a: '))
b=float(input('Enter b: '))
print(divide(a,b))



