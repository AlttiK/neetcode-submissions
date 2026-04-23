class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - k % len(nums)

        left = nums[:pivot]
        right = nums[pivot:]
        nums[:] = right + left
        
        