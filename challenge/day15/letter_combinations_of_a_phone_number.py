# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        
       
        
        num_dict = {1:[]
                    , 2:['a', 'b', 'c']
                    , 3:['d', 'e', 'f']
                    , 4:['g', 'h', 'i']
                    , 5:['j', 'k', 'l']
                    , 6:['m', 'n', 'o']
                    , 7:['p', 'q', 'r', 's']
                    , 8:['t', 'u', 'v']
                    , 9:['w', 'x', 'y', 'z']
                    , 0:[]
                   }
        
        if digits == "":
            return []
        
        def recursive(idx, temp):
            if temp:
                if len(temp) == len(digits):
                    answer.append(temp)
                    return 
       
            for i in num_dict[int(digits[idx])]:
                recursive(idx+1, temp+i)
        recursive(0,"")
        return answer
        