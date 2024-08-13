# https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
"""
Given a string s representing a valid expression,
implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""

"""
우선순위 
1. (
2. )
3. +, - 은 동일 
"""

class Solution:
    def remove_whitespace(self, s: str) -> str: 
        return s.replace(" ", "")
    
    def calculate(self, s: str) -> int:
        # 1. 후위 표현식으로 변환하기 
        stack = []
        
        # 숫자가 작을수록 우선순위가 높음. 
        operator = {"(": 1, ")":2, "+":3, "-":3}
        s = self.remove_whitespace(s)
        # 숫자, 연산자로 분리해야 함 
        if s.isnumeric():
            return int(s)
        post_expr = [] # 후위 표현식
        for x in s: 
            if x.isnumeric():
                post_expr.append(x)
            else: 
                if not stack: # stack 이 비어있는 경우 
                    stack.append(x)
                else: 
                    if x == ")": 
                        while stack: 
                            t = stack.pop()
                            if t == "(":
                                break 
                            post_expr.append(t)
                    elif x == "(":
                        post_expr.append(x)
                    else:  
                        while stack:
                            top = stack[-1]
                            if operator[top] > operator[x]: # x 의 우선순위가 더 높다면  
                                stack.append(x)
                            else: # 같거나 우선순위 낮은 경우
                                post_expr.append(stack.pop())
                        stack.append(x)

        while stack:
            post_expr.append(stack.pop())
        print("### POSTFIX",post_expr)

        # 2. 변환된 후위 표현식을 계산하기 
        for x in post_expr:
            # 숫자 (피연산자) 이면 집어넣기 
            if x.isnumeric():
                stack.append(int(x))
            elif x in ["+", "-"] and len(stack) >= 2: # 연산자 

                b = stack.pop()
                a = stack.pop()
                if x == "+":
                    tmp = a + b
                else:
                    tmp = a - b
                stack.append(tmp)

        return stack.pop()
    
## TEST CODE
sol = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
# s = "1 + 1"
answer = sol.calculate(s)
print(answer)