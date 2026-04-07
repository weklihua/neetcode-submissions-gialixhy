class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total, zero_count = 1, 0
        for num in nums:
            if num:
                total *= num
            else:
                zero_count += 1
        res = [0] * len(nums)

        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = total

        elif zero_count == 0:
            for i in range(len(nums)):
                res[i] = total // nums[i]
        return res
        