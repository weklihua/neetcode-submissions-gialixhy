class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map ={}
        max_len = 0
        for num in nums:
            nums_map[num] = num + 1 # key is num, val is consecutive
        for key, val in enumerate(nums_map):
            length = 0
            while val in nums:
                val += 1
                length += 1
            if length > max_len:
                max_len = length 
        return max_len

        