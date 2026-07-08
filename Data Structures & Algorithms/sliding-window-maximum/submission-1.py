class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_l = []

        for r in range(len(nums) - k + 1):
            curr_wnw = nums[r:r+k]
            max_v = max(curr_wnw)
            max_l.append(max_v)
        return max_l