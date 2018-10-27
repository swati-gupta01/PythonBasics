#Bubble Sort algorithm

def bubblesort(arr):
    l = len(a)
    # swap=False
    for i in range(l):
        swap=False
        for j in range(0,l-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
        if swap==False:
            break

    return arr


# a=[5,9,1,4,6]
a=[1,2,3,4]

print(bubblesort(a))