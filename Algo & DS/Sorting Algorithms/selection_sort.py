#selection sort algorithm

def selectionSort(arr):
    for i in range(len(arr)):
        i_min=i
        for j in range(i+1,len(arr)):
            if arr[i_min]>arr[j]:
                i_min=j
        arr[i],arr[i_min]=arr[i_min],arr[i]
    return arr
a=[5,8,3,9,1]
print(selectionSort(a))