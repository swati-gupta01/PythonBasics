#Binary search through recurisve call

def binarySearch(arr,l,r,x):
    if r<l:
        return -1
    mid = int((l+r)/2)
    print("mid:{}".format(mid))

    if arr[mid]==x:
        return mid
    elif arr[mid]>x:
        print('going to left')
        return binarySearch(arr,l,mid-1,x)
    elif arr[mid]<x:
        print('going to right')
        return binarySearch(arr,mid+1,r,x)
    else:
        return -1

arr=[1,2,3,4,5,6,10]
print(binarySearch(arr,0,len(arr)-1,52))