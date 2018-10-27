def insertion(arr):
    l=len(arr)
    for i in range(1,l):
        val=arr[i]
        hole=i
        while hole>0 and val<arr[hole-1]:
            arr[hole]=arr[hole-1]
            hole=hole-1
        arr[hole]=val
    return arr

print(insertion([3,4,1,9,0]))