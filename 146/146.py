from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()
        # oldest at the top, latest at the end

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1  

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
            self.dict[key] = value
        else:
            if len(self.dict) == self.capacity:
                self.dict.popitem(last = False)
            self.dict[key] = value
            