"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(array, l, r):
    p = array[r]
    ip = l
    for i in range(l, r):
        if array[i] < p:
            array[i], array[ip] = array[ip], array[i]
            ip += 1
    array[r], array[ip] = array[ip], array[r]
    # print array
    # print array[ip]
    return ip


def quicksort(array,l,r):

    if l < r:
        ip = partition(array, l, r)
        quicksort(array,0,ip-1)
        quicksort(array,ip+1,r)

    return array

# test = [21,5,4,1]
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test,0,len(test)-1))