#Bubble Sort algorithm

def bubblesort(arr):
    l = len(a)
    swap=False
    for i in range(l):
        for j in range(i+1,l):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
                swap=True
        if swap==False:
            break

    return arr


# a=[5,9,1,4,6]
a=[1,2,3,4]

print(bubblesort(a))