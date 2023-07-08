# Brute force with O(n2)
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(twosum(nums, target))

def twosum(nums, target):
    next_map = {}
    for i in range(len(nums)):
        next = target - nums[i]
        if next in next_map:
            return [next_map[next], i]
        next_map[nums[i]] = i


nums = [5,1, 2, 7]
target = 8
print(twosum(nums, target))
