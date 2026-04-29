class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            seen.add(n)

        longestSeq = 0

        for n in nums:
            start = n
            currSeq = 1
            while start + 1 in seen:
                currSeq += 1
                start += 1
            longestSeq = max(longestSeq, currSeq)
        
        return longestSeq