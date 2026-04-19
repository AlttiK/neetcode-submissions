class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        middle = len(nums) // 2

        left = self.sortArray(nums[0:middle])
        right = self.sortArray(nums[middle:len(nums)])

        return self.mergeSort(left, right)
    
    def mergeSort(self, left, right):
        sortedArray = []

        while left and right:
            if left[0] > right[0]:
                smaller = right.pop(0)
                sortedArray.append(smaller)
            else:
                smaller = left.pop(0)
                sortedArray.append(smaller)

        while left:
            val = left.pop(0)
            sortedArray.append(val)

        while right:
            val = right.pop(0)
            sortedArray.append(val)
        
        return sortedArray