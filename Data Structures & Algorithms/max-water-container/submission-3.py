class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_s = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            current_s = h * w
            max_s = max(max_s, current_s)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1 
        return max_s