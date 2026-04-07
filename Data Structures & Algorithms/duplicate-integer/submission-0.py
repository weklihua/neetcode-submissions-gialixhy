class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}
        if not nums: 
            return False
        for num in nums:
            if num in dupMap:
                return True
            else:
                dupMap[num] = 1
        return False
