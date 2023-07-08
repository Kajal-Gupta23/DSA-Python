# divide the given array then apply insertion sort
def sellsort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            current_ele = arr[i]
            pos = i
            while pos >= gap and current_ele > arr[pos - gap]:
                arr[pos] = arr[pos - gap]
                pos = pos - gap

            arr[pos] = current_ele
        gap = gap // 2


arr = [3, 2, 6, 1, 8]
sellsort(arr)

print(arr)
