def binary(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if (arr[mid] < x):
            low = mid + 1
        elif (arr[mid] > x):
            high = mid - 1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6]
x = 4
ans = binary(arr,x)
print(ans)
