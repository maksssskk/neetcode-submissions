class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        l = 0
        r = len(A) - 1
        while True:
            amid = (l+r) // 2
            bmid = half - amid - 2

            n1_l = A[amid] if amid >= 0 else float('-inf')
            n1_r = A[amid + 1] if (amid + 1) < len(A) else float('inf')
            n2_l = B[bmid] if bmid >= 0 else float('-inf')
            n2_r = B[bmid + 1] if (bmid + 1) < len(B) else float('inf')

            if n1_l <= n2_r and n2_l <= n1_r:
                if total % 2:
                    return min(n1_r, n2_r)
                else:
                    return (max(n1_l, n2_l) + min(n1_r, n2_r)) / 2
            elif n1_l > n2_r:
                r = amid - 1
            else: 
                l = amid + 1
        