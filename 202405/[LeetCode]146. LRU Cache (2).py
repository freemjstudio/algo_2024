from collections import OrderedDict 

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict() 
    
    def get(self, key:int):
        if key not in self.cache:
            return -1 
        value = self.cache[key] 
        # update 
        del self.cache[key] 
        self.cache[key] = value 
        return value 
    
    def put(self, key:int, value:int):
        if key in self.cache: 
            del self.cache[key]
            self.cache[key] = value 
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value 
            else: 
                # 멘 처음 요소 pop 시키기 
                self.cache.popitem(last=False)
                self.cache[key] = value 
        
        