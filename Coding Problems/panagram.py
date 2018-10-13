# https://www.geeksforgeeks.org/using-set-python-pangram-checking/

st='abcdefghijklmnopqrstuvwxyz'



def match(str1,str2):
    # str1=set(str1)
    str1=''.join(set(str1.replace(' ','').lower()))
    str=str1.lower()+str2
    t=0
    for i in str:
        t=t^ord(i)
    return t

print(match('The quick brown fox jumps over the lazy dog',st))
# print(match(st,st))