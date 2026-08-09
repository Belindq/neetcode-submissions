class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist =math.sqrt(x*x + y*y)
            print(x,y, dist)
            heapq.heappush(heap, (dist, points[i]))
        for j in range(k):
            dist, point = heapq.heappop(heap)
            print (dist, point)
            output.append(point)

        return output
