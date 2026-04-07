class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash = {}
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0)
            if nums_hash[num] == 1:
                return True
            else:
                nums_hash[num] += 1
        return False
        