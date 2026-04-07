class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        sorted_res = dict(sorted(res.items(), key=lambda item:item[1], reverse = True))
        k_most = []
        for key in sorted_res.keys():
            if k > 0:
                k_most.append(key)
                k -= 1
            else:
                break
        return k_most