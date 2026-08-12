class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_s = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                c = stack.pop()
                if stack:
                    s = heights[c] * (i - stack[-1] - 1)
                    max_s = max(max_s, s)
                else:
                    s = heights[c] * i
                    max_s = max(max_s, s)
            stack.append(i)
        while stack:
            c = stack.pop()
            if stack:
                s = heights[c] * (len(heights) - stack[-1] - 1)
            else:
                s = heights[c] * len(heights)
            max_s = max(max_s, s)
        return max_s