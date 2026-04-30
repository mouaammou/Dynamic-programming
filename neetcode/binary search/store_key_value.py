class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append((timestamp, value))
        # print(self.key_store)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        values = self.key_store[key]
        
        res = "" 
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2
            v_time = int(values[mid][0])
            v_value = values[mid][1]
            if v_time <= timestamp:
                res = v_value
                left = mid + 1
            else:
                right = mid - 1
            
        return res




Input = ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# process the input
for i in range(len(Input)):
    if Input[i] == "TimeMap":
        time_map = TimeMap()
    elif Input[i] == "set":
        key, value, timestamp = Input[i + 1]
        time_map.set(key, value, timestamp)
    elif Input[i] == "get":
        key, timestamp = Input[i + 1]
        print(time_map.get(key, timestamp))