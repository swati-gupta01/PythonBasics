def merge(arr):
        l=len(arr)
        if l<2:
            return arr
        m=(l-1)//2
        left=arr[0:m+1]
        right=arr[m+1:l]
        merge(left)
        merge(right)
        sort(arr,left,right)
        return arr

def sort(arr,l,r):
    nL=len(l)
    nR=len(r)
    i=j=k=0
    while i<nL and j<nR:
        if l[i]<r[j]:
            arr[k]=l[i]
            i+=1
        elif l[i]>r[j]:
            arr[k]=r[j]
            j+=1
        k+=1

    while i<nL:
        arr[k]=l[i]
        i+=1
        k+=1

    while j < nR:
        arr[k] = r[j]
        j += 1
        k += 1

print(merge([11,4,3,2,9,6]))