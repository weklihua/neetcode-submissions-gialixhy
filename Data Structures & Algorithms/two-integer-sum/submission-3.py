class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_map = {}
        for i in range(len(nums)):
            if nums[i] in res_map:
                return [res_map[nums[i]], i]
            sub = target - nums[i]
            
            if sub in res_map:
                continue
            res_map[sub] = i  