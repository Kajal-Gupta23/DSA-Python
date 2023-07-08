# we have to start iteration from the second element

def insertionsort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


arr = [5, 4, 1, 3, 2, 7, 0]
print(insertionsort(arr))
