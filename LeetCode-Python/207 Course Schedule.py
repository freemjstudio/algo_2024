"""
https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses

"""

from types import List 

# Cycle 판별 문제 ! Cycle 없으면 True, 있으면 False 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parents = [node for node in range(numCourses)] # 루트 노드를 자기 자신으로 설정
        answer = False 

        def find(x):
            if parents[x] != x: # 현재 node가 root node가 아니라면
                return find(parents[x]) # 재귀함수를 호출한다. 
            return x    # root node 
        
        # 두 원소가 속한 집합을 하나로 합친다. 
        def union(a, b):
            a = find(a)
            b = find(b)
            
            if a < b:
                parents[b] = a
            else: 
                parents[a] = b

        for a, b in prerequisites:
            # b -> a : b 를 들어야 a를 들을 수 있다. 
            union(a, b)

        return answer

# class Solution:

#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         parents = [node for node in range(numCourses)] # 루트 노드를 자기 자신으로 설정
#         answer = False 

#         def find(x):
#             if parents[x] != x: # 현재 node가 root node가 아니라면
#                 return find(parents[x]) # 재귀함수를 호출한다. 
#             return x    # root node 
        
#         # 두 원소가 속한 집합을 하나로 합친다. 
#         def union(a, b):
#             a = find(a)
#             b = find(b)
            
#             if a < b:
#                 parents[b] = a
#             else: 
#                 parents[a] = b

#         for a, b in prerequisites:
#             # b -> a : b 를 들어야 a를 들을 수 있다. 
#             union(a, b)

#         return answer
