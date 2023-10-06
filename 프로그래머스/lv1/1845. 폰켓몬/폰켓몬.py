def solution(nums):
    length = len(nums) / 2
    nums = set(nums)
    
    if length < len(nums):
        return length
    else:
        return len(nums) 