import collections

def moveZeroes(nums):
    i = 0
    N = len(nums)
    while i < N:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            N-=1
        else:
            i += 1

    return nums


print(moveZeroes([5,0,1,0,8]))

