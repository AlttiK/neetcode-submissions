class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = collections.defaultdict(int)
        maxHeap = []
        res = []

        for num in nums:
            freqDict[num] += 1
        
        for key in freqDict:
            maxHeap.append([-freqDict[key], key])
        
        heapq.heapify(maxHeap)

        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res