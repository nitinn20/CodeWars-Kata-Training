def solution(nums):
    if nums is not None:
        nums.sort()
        return nums
    else:
        return []