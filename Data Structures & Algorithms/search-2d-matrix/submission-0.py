class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        for l in matrix:
            for el in l:
                m.append(el)
        l = 0
        r = len(m) - 1

        while l <= r:
            mid = (l + r) // 2
            if m[mid] == target:
                return True
            elif m[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False