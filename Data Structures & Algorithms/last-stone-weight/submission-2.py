class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
            return stones[0]
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        print(heap)    
        while len(heap)>1:
            x= heapq.heappop(heap)
            y= heapq.heappop(heap)
            if x<y:
                heapq.heappush(heap,(x-y))
        if len(heap)>0:
            return -heap[0]
        return 0
