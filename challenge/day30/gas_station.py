"""
There are n gas stations along a circular route, 
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be unique

example 1 

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

example 2

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
"""

from typing import List 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0 # 순환하면서 total gas 를 누적해 나감 
        total_cost = 0 # 순환하면서 total cost를 누적해 나감 
        current_gas = 0 # 현재 tank 에 있는 gas 상태 
        start_index = 0 # potential starting index for the journey 

        # simulate 
        # 모든 potential starting index 를 검사하지는 않는다. 
        # -> 이는 불필요함. 총 가스 양이 총 비용 보다 작으면 어느 시작점이든 전체 주유소를 순회하는 것이 불가능하기 때문이다. 
        for i in range(len(gas)):
            total_gas += gas[i] 
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
        
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0

        if total_gas < total_cost:
            return -1
        else:
            return start_index

"""

총 가스와 총 비용을 계산:

총 가스: 1 + 2 + 3 + 4 + 5 = 15
총 비용: 3 + 4 + 5 + 1 + 2 = 15
따라서 총 가스가 총 비용과 같으므로, 순환이 가능하다는 것을 알 수 있습니다.

현재 가스를 계산하며 순회:

i=0: current_gas = 1 - 3 = -2 (음수이므로 시작점 갱신)
i=1: current_gas = 2 - 4 = -2 (음수이므로 시작점 갱신)
i=2: current_gas = 3 - 5 = -2 (음수이므로 시작점 갱신)
i=3: current_gas = 4 - 1 = 3 (음수 아님)
i=4: current_gas = 3 + 5 - 2 = 6 (음수 아님)

"""

#### Test Case 1 

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

s = Solution()
answer = s.canCompleteCircuit(gas=gas, cost=cost)
print(answer)


