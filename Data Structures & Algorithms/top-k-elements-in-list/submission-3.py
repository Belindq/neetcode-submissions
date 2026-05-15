class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        for num in nums:
            count[num] +=1
        heap = [(-v,k) for k, v in count.items()]
        heapq.heapify(heap)
        final =[]
        for i in range(k):
            final.append(heapq.heappop(heap)[1])
        return final