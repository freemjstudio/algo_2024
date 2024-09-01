"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""

from typing import List 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0 
        hold_stock = False # 주식 가지고 있는 경우 
        # 증가하는 부분 수열 중 profit 이 최대인 것
        buy_price = 0 

        n = len(prices)
        for i in range(n-1):
            # 지금이 최저가인 경우 
            if prices[i] < prices[i+1] and not hold_stock:
                hold_stock = True
                buy_price = prices[i]
            elif prices[i] > prices[i+1] and hold_stock:
                hold_stock = False 
                sell_price = prices[i]

                answer += (sell_price - buy_price)

        # 아직 가지고 있다면 
        if hold_stock:
            sell_price = prices[n-1]
            answer += (sell_price - buy_price)

        return answer 