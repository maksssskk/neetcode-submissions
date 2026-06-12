class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for char in nums:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        sort = sorted(d, key=lambda x: d[x], reverse=True)
        result = sort[0:k]
        return result