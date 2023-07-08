def linear(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return (i)

    return -1


arr = [1, 2, 4, 5, 1, 3]
x = 3
print(linear(arr, x))
