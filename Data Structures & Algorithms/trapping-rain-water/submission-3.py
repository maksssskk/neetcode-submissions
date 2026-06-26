class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        s = 0
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                s += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                s += rmax - height[r]

        return s

