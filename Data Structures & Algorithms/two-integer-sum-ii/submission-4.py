class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            currNum = numbers[left] + numbers[right]
            if currNum == target:
                return [left + 1, right + 1]
            elif currNum > target:
                right -= 1
            else:
                left += 1
        
        return [left + 1, right + 1]