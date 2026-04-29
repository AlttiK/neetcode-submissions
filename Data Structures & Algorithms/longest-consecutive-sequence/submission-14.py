class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        starts = []

        for n in nums:
            seen.add(n)
        
        for n in nums:
            if n - 1 not in seen:
                starts.append(n)
        
        longestSeq = 0
        currSeq = 1
        for n in starts:
            while n+1 in seen:
                n += 1
                currSeq += 1
            longestSeq = max(longestSeq, currSeq)
            currSeq = 1

        return longestSeq



        