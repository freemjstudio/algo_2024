# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key 
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None # -> least recently used node 
        self.tail = None # -> most recently used node
        
    # insert 
    def insert(self, node):
        # check head 
        if self.head == None: 
            self.head = node
        else:
            self.tail.next = node 
            node.prev = self.tail 
        self.tail = node # 최신 삽입한 노드 
        
    # delete 
    def delete(self, node):
        if node.prev: # 삭제할 노드의 previous 노드 확인 
            node.prev.next = node.next 
        else: 
            self.head = node.next 
        if node.next: # 삭제할 노드의 next 노드 확인 
            node.next.prev = node.prev 
        else: 
            self.tail = node.prev
            
        
class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity 
        self.cache = {} # O(1) 시간으로 데이터에 접근 , key: Node
        self.linkedlist = LinkedList() # least recently used 정보 저장 
    
    # update linkedlist with new node 
    def update(self, key:int, val:int):
        node = Node(key=key, val=val)               # (3)
        self.cache[key] = node
        self.linkedlist.insert(node) 
        
    
    def get(self, key: int) -> int:
        # (1) list 에서 node 찾은 후 val 구하기 
        # (2) node 삭제, 
        # (3) linkedlist 맨 뒤에 노드를 append 시켜서 최근 사용 업데이트하기 
        if key in self.cache:
            value = self.cache[key].val                   # (1)
            self.linkedlist.delete(self.cache[key])     # (2)
            self.update(key=key, val=value)
            return value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        # update the value of the key if the key exists 
        if key in self.cache:
            self.linkedlist.delete(self.cache[key])
        else:  
            if len(self.cache) >= self.capacity: # cache 의 capacity가 남아있는 경우
                del self.cache[self.linkedlist.head.key]
                self.linkedlist.delete(self.linkedlist.head)
                
        # insert updated node 
        self.update(key=key, val=value)

            