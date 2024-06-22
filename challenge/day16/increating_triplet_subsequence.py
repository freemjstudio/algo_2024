
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = 2**31, -2**31
        
        for third in nums: 
            if first < second < third: 
                print(first, second, third)
                return True # 정렬 성공 
            if third <= first: # 같은 숫자는 갱신해야 함 
                first = third
            else: 
                second = third
              
        return False  
        