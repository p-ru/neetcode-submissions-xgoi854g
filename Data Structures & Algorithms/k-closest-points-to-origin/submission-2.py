class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:

            key = point[0]**2 + point[1]**2
            heapq.heappush_max(pq, (key, point))
            while len(pq) > k:
                heapq.heappop_max(pq)
        return [point for _, point in pq]