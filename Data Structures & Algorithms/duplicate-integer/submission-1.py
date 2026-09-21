class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testSet = set()
        for n in nums:
            if n in testSet:
                return True
            testSet.add(n)
        
        return False