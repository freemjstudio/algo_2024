
"""
https://leetcode.com/problems/time-based-key-value-store/description/

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. 
If there are no values, it returns "".

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.
"""

# class TimeMap:
#     def __init__(self):
#         self.store = dict()
        
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.store: 
#             self.store[key] = dict()
#         self.store[key][timestamp] = value 

#     def get(self, key: str, timestamp: int) -> str:
        
#         if timestamp in self.store[key].keys(): 
#             return self.store[key][timestamp]
#         else: 
#             # 없으면 가장 앞에 있는 값을 리턴한다. 
#             last_key, last_value = None, None 
#             key_list = list(self.store[key].keys())
                            
#             if key_list: 
#                 if key_list[0] > timestamp:
#                     return ""
#                 for k, v in self.store[key].items():
#                     if k: 
#                         if k < timestamp:
#                             last_key, last_value = k, v
#                         else: 
#                             break 
#                     else: 
#                         break 
                    
#                 return last_value
#             else: # 아예 값이 없는 경우 
#                 return ""
         
        
# d = {1:'a', 2:'b', 3:'c'}
# for k, v in d.items():
#     print(k, v)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# 통과된 풀이 

from collections import defaultdict 

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list) 
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        # timestamp info 
        ts_log = self.store[key] 
        
        if len(ts_log) == 0 or ts_log[0][1] > timestamp: 
            return "" 
        
        # timestamp 보다 작으면서, timestamp 와 가장 가까운 시간의 값을 탐색 
        # binary search O(logN)
        answer = ""
        left, right = 0, len(ts_log)

        while left <= right and left < len(ts_log):
            mid = (left+right)//2
     
            if ts_log[mid][1] == timestamp:
                return ts_log[mid][0]
            elif ts_log[mid][1] < timestamp:
                answer = ts_log[mid][0]
                left = mid + 1
            else: 
                right = mid -1
          
        return answer 