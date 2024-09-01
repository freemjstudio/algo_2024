"""

https://leetcode.com/problems/queue-reconstruction-by-height/description/

You are given an array of people, people, 
which are the attributes of some people in a queue (not necessarily in order).
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki 
other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. 
The returned queue should be formatted as an array queue, 
where queue[j] = [hj, kj] is the attributes of the jth person in the queue 
(queue[0] is the person at the front of the queue).

Example 1:

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

"""

from typing import List

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people.sort(key=lambda x:(-x[0], x[1])) # 이렇게하면 키가 큰 순서대로 정렬된다. 
print(people)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        people.sort(key=lambda x:(-x[0], x[1])) # [[5, 0], [7, 0], [6, 1], [7, 1], [5, 2], [4, 4]]
        
        for p in people: 
            answer.insert()
        return answer
    
# ## TEST CASE

# sol = Solution()
# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# answer = sol.reconstructQueue(people)