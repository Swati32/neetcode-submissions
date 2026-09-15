class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            mid_time, mid_val = values[mid]

            if mid_time == timestamp:
                return mid_val
            elif mid_time < timestamp:
                res = mid_val   # Valid floor candidate; save it
                l = mid + 1     # Try to find a newer/larger valid timestamp
            else:
                r = mid - 1     # Future timestamp; look left

        return res
        
