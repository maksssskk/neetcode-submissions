class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        l, r = 0, len(height) - 1
        s = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_wall:
                    l_wall = height[l]
                else:
                    s += l_wall - height[l]
                l += 1
            else:
                if height[r] >= r_wall:
                    r_wall = height[r]
                else:
                    s += r_wall - height[r]
                r -= 1
        return s

