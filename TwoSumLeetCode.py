nums = [2,7,11,15]
target = 9


def twosum(nums, target):
    seen = {}

    for i , num in enumerate(nums):
        complement = target - num
        if complement in seen:
             print(f"[seen[complement], {i}]")
        seen[num] = i



