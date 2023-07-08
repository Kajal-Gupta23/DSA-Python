def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)


arr = [1, 2, 2, 6, 2, 4, 7]
print(mergesort(arr))
