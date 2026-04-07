class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        
        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/k)
            if total_time <= h:
                res = k
                r = k - 1
            elif total_time > h:
                l = k + 1
        return res

