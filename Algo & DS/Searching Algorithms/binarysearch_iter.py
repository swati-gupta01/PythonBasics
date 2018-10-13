def binary_search(input_array, value):
    l=len(input_array)
    # print(mid)
    left=0
    right=l-1
    while left<=right:
        mid = (left+right) // 2
        if input_array[mid]==value:
            return mid
        if value<input_array[mid]:
            right=mid-1
            # print(mid)
        elif value>input_array[mid]:
            left=mid+1
            # print(mid)

    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))


