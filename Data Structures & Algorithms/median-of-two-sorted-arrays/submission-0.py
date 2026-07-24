class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        me = []
        me = sorted(nums1 + nums2)

        n = len(me)
        if n % 2 == 0:
            res = (me[n//2] + me[(n-1)//2]) / 2
            return float(res)
        else:
            res = me[n//2]
            return float(res)