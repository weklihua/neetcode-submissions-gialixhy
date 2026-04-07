from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            cur_area = width * height

            max_area = max(max_area, cur_area)

            # Move the pointer at the shorter line
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area