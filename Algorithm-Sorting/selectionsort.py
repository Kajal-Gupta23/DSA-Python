# inplace comparison based algo
# 1. search the list and find out the minimum number
# 2. we will say first value is smaller than we will compare it with rest values if we find any smaller value then we will set it to min
# 3. place the min value at 0th index
# 4. follow 2 and 3 again

def selectionsort(l):
    for i in range(len(l)):
        min_ind = i
        for j in range(i + 1, len(l)):
            if l[min_ind] > l[j]:
                min_ind = j
            l[i], l[min_ind] = l[min_ind], l[i]

    return l


l = [6,3,2,5,4]
print(selectionsort(l))
