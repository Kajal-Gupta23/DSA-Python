def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]  = arr[j+1],arr[j]

    return arr

arr =[-6,3,1,7,2]
print(bubblesort(arr))
