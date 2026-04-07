class Solution:
    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        
        return -1
         
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_nums = []
        for row in matrix:
            first_nums.append(row[0])
        
        t, b = 0, len(first_nums) - 1

        while t < b:
            m = (t + b) // 2
            if target > first_nums[m]:
                t = m + 1
            elif target < first_nums[m]:
                b = m - 1
            else:
                return True
        if first_nums[t] == target:
            return True
        elif first_nums[t] > target:
            res = self.binarySearch(matrix[t - 1], target)
        else:
            res = self.binarySearch(matrix[t], target)
        return True if res > 0 else False
        