
#Using XOR operation

def find_order(str1,str2):
    if len(str1)!=len(str2):
        return -1
    str=str1+str2
    t=0
    for i in str:
        t=t^ord(i)
    return t


print(find_order('liqsten','silentq'))
