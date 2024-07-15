# https://leetcode.com/problems/sort-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # list 의 마지막 
            return head 
        
        # 두개의 리스트로 split 
        left = head 
        right = self.get_mid(head)
        tmp = right.next
        right.next = None 
        right = tmp 
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
        
    def get_mid(self, head):
        low, high = head, head.next 
        while high and high.next: 
            low = low.next 
            high = high.next.next
            
        return low 
    
    def merge(self, left, right):
        tail = dummy = ListNode()
        
        while left and right: 
            if left.val < right.val: 
                tail.next = left
                left = left.next 
            else: 
                tail.next = right
                right = right.next 
            tail = tail.next 
        # 남은 element 처리 
        if left: # not null 
            tail.next = left
        if right: 
            tail.next = right 
        return dummy.next 
        
        