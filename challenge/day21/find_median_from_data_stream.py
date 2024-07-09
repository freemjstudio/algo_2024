# 첫번째 시도 2266 ms

class MedianFinder:
    def __init__(self):
        self.arr = [] # 항상 정렬된 상태여야 함

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        
    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) % 2 == 1: # 홀수 
            mid = len(self.arr)//2
            return self.arr[mid]
        else: # 짝수인 경우 
            
            mid = len(self.arr)//2
            return (self.arr[mid] + self.arr[mid-1])/2

# 두번째 시도 347 ms

from heapq import * 
class MedianFinder:

    def __init__(self):
        # 최대힙과 최소힙을 두고 밸런싱을 해나간다. 
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
    # 최대힙이 비어 있는 경우 insert
    # 최대힙의 최대 값이 num 보다 크면 insert 
        if not self.max_heap or -self.max_heap[0] >= num:
            # 최대힙으로 사용하기 위해서는 음수로 처리해줘서 역정렬해주어야 함 
            heappush(self.max_heap, -num)
        else: 
            heappush(self.min_heap, num)
            
		    # 두개의 heap 을 balance 하는 과정  
        # max_heap 의 길이는 min_heap 보다 항상 같거나, 1만큼 더 길어야 한다. 
        # (중앙값을 구해야하기 떄문)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        

    def findMedian(self) -> float:
        # 짝수 인 경우 각각의 root 에서 빼주면 됨 
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0])/2.0
        else: 
            return (-self.max_heap[0])/1.0
        