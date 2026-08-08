class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq= defaultdict(int)
        new = ""
        wait = deque()
        for i in s:
            freq[i] +=1
        for j in freq:
            heapq.heappush(heap, (-freq[j], j))
        maxfreq = max(freq.values())
        if maxfreq > (len(s) + 1) // 2:
            return ""
        while heap:
            count, char = heapq.heappop(heap)
            new += char
            if wait:
                heapq.heappush(heap, wait.popleft())
            if count+1<0:
                wait.append((count+1, char))
 
        return new

    
        
