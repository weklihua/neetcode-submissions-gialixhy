class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []
        if not points:
            return minHeap
        for point in points:
            x, y = point
            dist = (x ** 2) + (y ** 2)
            one = [dist, x, y]
            minHeap.append(one)
        heapq.heapify(minHeap)

        while k > 0:
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res