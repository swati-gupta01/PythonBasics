#Bubble Sort algorithm

def bubblesort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(i+1,l):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr


a=[5,9,1,4,6]

print(bubblesort(a))



