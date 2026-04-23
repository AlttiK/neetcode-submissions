class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    currLeft = nums[left]
                    left += 1
                    while currLeft == nums[left] and left < right:
                        left += 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1
        return res


