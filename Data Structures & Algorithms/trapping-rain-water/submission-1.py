class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0

        for i in range(1, len(height) - 1):
            water = min(max(height[:i]), max(height[i+1:])) - height[i]
            if water <= 0:
                continue
            else:
                s += water
        return s