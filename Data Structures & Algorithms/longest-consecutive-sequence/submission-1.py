class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        current_streak = 1

        nums_sort = sorted(list(set(nums)))
        if not nums:
            return 0
        else:
            for i in range(len(nums_sort) - 1):
                if nums_sort[i+1] == nums_sort[i] + 1:
                    current_streak += 1
                else:
                    max_streak = max(max_streak, current_streak)
                    current_streak = 1
            
        return (max(max_streak, current_streak))