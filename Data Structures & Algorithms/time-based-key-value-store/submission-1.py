class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        val = self.d.get(key, [])

        l = 0 
        r = len(val) - 1
        while l <= r:
            mid = (l + r) // 2
            if val[mid][1] == timestamp:
                res = val[mid][0]
                return res
            elif val[mid][1] <= timestamp:
                res = val[mid][0]
                l = mid + 1 
            else:
                r = mid - 1
        return res