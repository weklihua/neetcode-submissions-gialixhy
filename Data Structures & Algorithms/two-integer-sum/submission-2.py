class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        if not nums:
            return None
        for i in range(len(nums)):
           
            if nums[i] not in myDict:
                
                res = target - nums[i]
                if res in myDict:
                    return [myDict[res], i]
                myDict[nums[i]] = i
            elif 2 * nums[i] == target:
                return [myDict[nums[i]], i]