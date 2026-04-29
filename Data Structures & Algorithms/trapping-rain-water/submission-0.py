class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxL = height[left]
        maxR = height[right]

        total = 0

        while left < right:
            if maxL <= maxR:
                left += 1
                maxL = max(maxL, height[left])
                total += max(maxL - height[left], 0)
            else:
                right -= 1
                maxR = max(maxR, height[right])
                total += max(maxR - height[right], 0)   
                    
        return total

