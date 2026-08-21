class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_targets = {}
        for i, num in enumerate(nums):
            new_target = target - num
            if new_target in new_targets:
                return [new_targets[new_target], i]
            new_targets[num] = i
        return